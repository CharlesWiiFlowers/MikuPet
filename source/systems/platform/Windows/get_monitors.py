import ctypes
from ctypes import wintypes

from systems.monitor_info import MonitorInfo


user32 = ctypes.windll.user32


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]



class MONITORINFO(ctypes.Structure):
    _fields_ = [
        ("cbSize", wintypes.DWORD),
        ("rcMonitor", RECT),
        ("rcWork", RECT),
        ("dwFlags", wintypes.DWORD),
    ]



def get_monitors():

    monitors = []


    def callback(
        hMonitor,
        hdcMonitor,
        lprcMonitor,
        dwData
    ):

        info = MONITORINFO()

        info.cbSize = ctypes.sizeof(MONITORINFO)


        if user32.GetMonitorInfoW(
            hMonitor,
            ctypes.byref(info)
        ):

            rect = info.rcMonitor

            monitor = MonitorInfo(
                name=f"Monitor {len(monitors)+1}",

                left=rect.left,
                top=rect.top,

                width=rect.right - rect.left,
                height=rect.bottom - rect.top
            )

            monitors.append(monitor)


        return True



    MonitorEnumProc = ctypes.WINFUNCTYPE(
        wintypes.BOOL,
        wintypes.HMONITOR,
        wintypes.HDC,
        ctypes.POINTER(RECT),
        wintypes.LPARAM
    )


    user32.EnumDisplayMonitors(
        None,
        None,
        MonitorEnumProc(callback),
        0
    )


    return monitors