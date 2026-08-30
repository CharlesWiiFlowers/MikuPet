"""
Get information about the active window on Windows.
"""
from core.events.event_bus import EventBus
from core.events.event_types import EVENT_ERROR
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


def get_active_window_rect(bus: EventBus) -> tuple[int, int, int, int, int, int]:
    """Returns (left, top, right, bottom, hwnd, pid) of the active window."""
    hwnd = user32.GetForegroundWindow()
    if hwnd == 0:
        return (0, 0, 0, 0, 0, 0)  # No active window found
    rect = RECT()

    if not user32.GetWindowRect(hwnd, ctypes.byref(rect)):
        bus.emit(EVENT_ERROR, f"Failed to get window rectangle. Detailed Error: {ctypes.WinError().args}", source=bus)
        return (0, 0, 0, 0, 0,0)
    return rect.left, rect.top, rect.right, rect.bottom, hwnd, get_window_pid(hwnd)

def get_window_pid(hwnd: int) -> int:
    pid = wintypes.DWORD()

    user32.GetWindowThreadProcessId(
        hwnd,
        ctypes.byref(pid)
    )

    return pid.value