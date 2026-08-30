"""
This module contains the WindowSystem class, which is responsible for managing window-related events and interactions within the application.
"""

from core.events.event_bus import EventBus
from core.events import event_types
from core.character import Character
import platform

from systems.platform.Windows.get_active_window import get_active_window_rect

class WindowSystem:
    def __init__(self, bus: EventBus, character: Character):
        self.bus = bus
        self.character = character
        self.os_name = platform.system()

        self.previous_window_rect = 0
        self.previous_window_rect_sides = (0,0,0,0)
        
        self.bus.on(event_types.ENGINE_PRE_UPDATE, self.check_window)

    def check_window(self, event):
        if self.os_name == "Windows":
            
            rect = get_active_window_rect(self.bus)

            if rect[4] != self.previous_window_rect or rect[0:4] != self.previous_window_rect_sides:
                self.previous_window_rect = rect[4]
                self.previous_window_rect_sides = rect[0:4]

                if self.character.get_PID() == rect[5]:
                    return
                
                self.bus.emit(
                    event_name=event_types.WINDOW_STATE_UPDATED,
                    data={'left': rect[0], 'top': rect[1], 'right': rect[2], 'bottom': rect[3], 'pid': rect[5]},
                    source=self
                )