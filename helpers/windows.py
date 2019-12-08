"""Active window's helper for Windows."""
from ctypes import windll, create_unicode_buffer

def get_active_window_title():
    """Return the tittle of the active window."""
    # Based on: https://stackoverflow.com/a/58355052
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)

    if buf.value:
        return buf.value
    else:
        return None

if __name__ == "__main__":
    print(get_active_window_title())
