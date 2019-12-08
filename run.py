"""Time Tracking App."""
import time
from datetime import datetime, timezone
from helpers import get_active_window_title
from models import Activity, TimeEntry

def main():
    """Main function."""
    activities = []
    actual_activity = get_active_window_title()
    actual_time_entry_start_time = datetime.now(timezone.utc)
    try:
        while True:
            activities, actual_activity, actual_time_entry_start_time = resume_activity(activities,
                                                                                        actual_activity,
                                                                                        actual_time_entry_start_time)          
            time.sleep(1)
    except KeyboardInterrupt:
        activities, actual_activity, actual_time_entry_start_time = resume_activity(activities,
                                                                                    actual_activity,
                                                                                    actual_time_entry_start_time)
        print("Resume:")
        print("")
        print("Activity\tTime Spent")
        print("________\t__________")
        
        for activity in activities:
            print(f"{activity.window_title.decode('utf8')}\t{activity.get_time_spent()}")


def resume_activity(activities, actual_activity, actual_time_entry_start_time):
    """Resume the actual activity."""
    current_activity = get_active_window_title()
    # Check if theres was a change in the activity
    if current_activity != actual_activity:
        # Look for if the activity exists
        for previus_activity in activities:
            if previus_activity.window_title == actual_activity:
                break
        else:
            previus_activity = None

        previus_activity_time_entry = TimeEntry(start_time=actual_time_entry_start_time,
                                                end_time=datetime.now(timezone.utc))
        # If not exist the activity, it'll be created
        if not previus_activity:
            previus_activity = Activity(actual_activity)
            activities.append(previus_activity)

        # Add the time entry for the activity
        previus_activity.add_time_entry(previus_activity_time_entry)
        # Set the new actual activity
        actual_activity = current_activity
        actual_time_entry_start_time = datetime.now(timezone.utc)
    return activities, actual_activity, actual_time_entry_start_time


if __name__ == "__main__":
    main()
