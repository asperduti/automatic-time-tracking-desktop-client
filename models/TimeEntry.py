"""Model for Time Entry."""
import json


class TimeEntry():
    """Class for TimeEntry."""
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time


    def total_time(self):
        """Calculate the total time for the time entry."""
        return self.end_time - self.start_time


    def serialize(self):
        """Serialize the TimeEntry."""
        return {
            'start_time' : self.start_time.strftime("%Y-%m-%d %H:%M:%S%Z%z"),
            'end_time' : self.end_time.strftime("%Y-%m-%d %H:%M:%S%Z%z")
        }


    def to_json(self):
        """Return a JSON from the serialize."""
        return json.dumps(self.serialize())
