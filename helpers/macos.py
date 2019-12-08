"""Active window's helper for MacOs."""
from AppKit import NSWorkspace


def get_active_window_title():
    """Return the tittle of the active window."""
    # Based on: http://stackoverflow.com/a/373310/562769
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    return activeAppName

if __name__ == "__main__":
    print(get_active_window_title())
