import sys


if sys.platform in ['linux', 'linux2']:
    from .linux import get_active_window_title
elif sys.platform in ['Windows', 'win32', 'cygwin']:
    from .windows import get_active_window_title
elif sys.platform in ['Mac', 'darwin', 'os2', 'os2emx']:
    from .macos import get_active_window_title
else:
    print(f"sys.platform={sys.platform} not supported. Please report.")
