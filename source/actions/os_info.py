"""
Get system information to help Miku understand the environment she is running in.
"""

import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]


def get_active_window_rect() -> tuple[int, int, int, int]:
    """Returns (left, top, right, bottom) of the active window."""

    hwnd = user32.GetForegroundWindow()
    if hwnd == 0:
        return (0, 0, 0, 0)

    rect = RECT()

    if not user32.GetWindowRect(hwnd, ctypes.byref(rect)):
        raise ctypes.WinError()

    return rect.left, rect.top, rect.right, rect.bottom