"""Model for the Activities."""
from datetime import datetime, timezone, timedelta
import json


class Activity():
    """Class to represent an Activity."""

    def __init__(self, window_title):
        """Constructor."""
        self.window_title = window_title
        self.time_entries = []


    def add_time_entry(self, time_entry):
        """Method to add a time entry."""
        self.time_entries.append(time_entry)


    def get_time_entries(self, start_time=datetime.min.replace(tzinfo=timezone.utc),
                         end_time=datetime.max.replace(tzinfo=timezone.utc)):
        """Return all the time entries between start_time and end_time."""
        return [time_entry for time_entry in self.time_entries if time_entry.start_time <= end_time and time_entry.end_time >= start_time]


    def get_time_spent(self, start_time=datetime.min.replace(tzinfo=timezone.utc),
                       end_time=datetime.max.replace(tzinfo=timezone.utc)):
        """Return the time spent in the interval given."""
        time_entries = self.get_time_entries(start_time=start_time, end_time=end_time)
        time_spent = timedelta()
        for time_entry in time_entries:
            # To give the time spent beetween start_time and end_time
            # we need to check if the time entry begin before of after start_time, 
            # and the same for the end of the time_entry, but with the end_time.
            if time_entry.start_time >= start_time and time_entry.end_time <= end_time:
                time_spent += time_entry.end_time - time_entry.start_time
            elif time_entry.start_time <= start_time and time_entry.end_time <= end_time:
                time_spent += time_entry.end_time - start_time
            elif time_entry.start_time >= start_time and time_entry.end_time >= end_time:
                time_spent += end_time - start_time
            elif time_entry.start_time <= start_time and time_entry.end_time >= end_time:
                time_spent += end_time - start_time
            else:
                raise Exception("Invalid option.")

        return time_spent


    def serialize(self, start_time=datetime.min.replace(tzinfo=timezone.utc),
                  end_time=datetime.max.replace(tzinfo=timezone.utc)):
        """Serialice the instance."""
        return {
            'window_title' : self.window_title.decode('utf-8'),
            'time_entries' : [time_entry.serialize() for time_entry in self.get_time_entries(start_time=start_time,
                                                                                             end_time=end_time)],
            'time_spent' : self.get_time_spent(start_time=start_time,
                                               end_time=end_time).total_seconds()
        }


    def to_json(self, start_time=datetime.min.replace(tzinfo=timezone.utc),
                end_time=datetime.max.replace(tzinfo=timezone.utc)):
        """Return the JSON object from the serialize."""
        return json.dumps(self.serialize(start_time=start_time,
                                         end_time=end_time))
