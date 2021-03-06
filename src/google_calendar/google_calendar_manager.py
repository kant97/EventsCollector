import datetime
import itertools
import json
import logging
import time

from oauth2client import file

# If modifying these scopes, delete the file token.json.
import configs_worker

SCOPES = 'https://www.googleapis.com/auth/calendar'


def _extract_target_calendars_ids(all_calendars_info, target_calendars_names):
    res = []
    target_names_set = set(target_calendars_names)
    need_primary = False
    if 'primary' in target_names_set:
        need_primary = True
    for resource in all_calendars_info:
        their_calendar_name = resource['summary']
        if their_calendar_name in target_names_set:
            res.append(resource['id'])
            target_names_set.remove(their_calendar_name)
        if need_primary and resource.get('primary', False):
            res.append(resource['id'])
            target_names_set.remove('primary')
            need_primary = False
    return res


class GoogleCalendarManager:

    def __init__(self, gc_client):
        self.client = gc_client

    # Returns google api service
    def authenticate(self):
        store = file.Storage('google_calendar/token.json')
        creds = store.get()
        if not creds or creds.invalid:
            creds = self.client.do_authentication_flow(store)
        return self.client.do_authenticate(creds)

    # Returns dictionary of json object with not more then N upcoming events
    def get_n_upcoming_events(self, eventsAmount):
        logging.info('Getting the upcoming {0} events'.format(eventsAmount))
        events = self.client.get_upcoming_events('primary', eventsAmount)

        if not events:
            logging.info('No upcoming events found.')
            return None
        return events

    # Returns list with all-day events planed for date = date_iso
    def get_all_day_events(self, date_iso):
        t = time.strptime(date_iso, "%Y-%m-%d")
        day = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)

        start_day_time_str = day.isoformat()
        start_day_time_str += 'T00:00:00Z'
        end_day_time_str = day.isoformat()
        end_day_time_str += 'T00:01:00Z'
        config = configs_worker.load_configs_from_disc()
        events_for_today = []
        calendars_list_to_process = config['my_calendars']

        all_calendars_info = self.client.get_all_calendars_ids()
        calendar_ids = _extract_target_calendars_ids(all_calendars_info, calendars_list_to_process)

        for c in calendar_ids:
            c_today_events = self.client.get_todays_allday_events(c, start_day_time_str, end_day_time_str, True)
            if c_today_events is not None:
                events_for_today = itertools.chain(events_for_today, c_today_events)
        all_days = []
        if events_for_today is not None:
            for event in events_for_today:
                if event['start'].get('dateTime') is None:
                    all_days.append(event)
        return all_days

    # Returns list with all all-day events for today
    def get_todays_all_day_events(self):
        return self.get_all_day_events(datetime.date.today().isoformat())

    # Accepts event_name_str as string, date_str in ISO format (like 2018-09-26), time_str (like H:M:S), ...
    # Return None with ok and error_str if not
    def post_event(self, event_name_str, date_str, time_str=None, color_id_str=None, event_description_str=None):
        if time_str is not None:
            t = time.strptime(date_str + " " + time_str, "%Y-%m-%d %H:%M:%S")
        else:
            t = time.strptime(date_str, "%Y-%m-%d")
        end_date_str = datetime.date(t.tm_year, t.tm_mon, t.tm_mday)
        end_date_str += datetime.timedelta(days=1)

        # Configuring event
        if time_str is None:
            start = {"date": date_str}
            end = {"date": end_date_str.isoformat()}
        else:
            start = {"dateTime": date_str + "T" + time_str, "timeZone": "Europe/Moscow"}
            end = {"dateTime": date_str + "T" + datetime.time(t.tm_hour + 1, t.tm_min, t.tm_sec).isoformat(),
                   "timeZone": "Europe/Moscow"}

        logging.info("start: " + json.dumps(start))
        logging.info("end: " + json.dumps(end))

        body = {
            "end": end,
            "start": start,
            "summary": event_name_str,
            "reminders": {
                "overrides": "",
                "useDefault": "false"
            }
        }
        if event_description_str is not None:
            body["description"] = event_description_str
        if color_id_str is not None:
            body['colorId'] = color_id_str

        logging.info("Posting event with name {0} to google calendar".format(event_name_str))
        resp_error = self.client.post_event(body)
        logging.info("Done")
        return resp_error
