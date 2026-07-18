"""
This module contains the WindowSystem class, which is responsible for managing window-related events and interactions within the application.
"""

from core.events.event_bus import EventBus
from core.events import event_types
import platform

from systems.platform.window.get_active_window import get_active_window_rect

class WindowSystem:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.os_name = platform.system()
        
        self.bus.on(event_types.ENGINE_PRE_UPDATE, self.check_window)

    def check_window(self, event):
        if self.os_name == "Windows":
            
            rect = get_active_window_rect(self.bus)
            
            self.bus.emit(
                event_name=event_types.WINDOW_STATE_UPDATED,
                data={'left': rect[0], 'top': rect[1], 'right': rect[2], 'bottom': rect[3]},
                source=self
            )