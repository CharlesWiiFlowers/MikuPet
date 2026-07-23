"""
Logs System
"""

from pathlib import Path

from core.events.event_bus import EventBus
from core.events.event_types import EVENT_ERROR, ENGINE_PRE_UPDATE, ENGINE_UPDATE, ENGINE_RENDER, EVENT_POSITION_CHANGED, WINDOW_STATE_UPDATED, EVENT_SPRITE_FRAME_CHANGED
from core.events.events import Event

class Logger():
    def __init__(self, bus:EventBus) -> None:
        self.bus = bus

        self.enable_engine_logs = False  # Flag to enable or disable engine logs

        self.bus.on_all(
            callback=self.write_log
        )

        self.project_root = Path(__file__).resolve().parent.parent.parent
        self.log_dir = self.project_root / "data"
        self.log_file = self.log_dir / "events.log"
        self.log_long_file = self.log_dir / "detailed_events.log"

        self.log_dir.mkdir(exist_ok=True)
    
    def write_log(self, event:Event):

        # TODO: Add a blacklist
        if not self.enable_engine_logs and event.event_type in [ENGINE_PRE_UPDATE, ENGINE_UPDATE, ENGINE_RENDER, WINDOW_STATE_UPDATED, EVENT_SPRITE_FRAME_CHANGED, EVENT_POSITION_CHANGED]:
            return  # Skip logging for engine events if disabled

        with open(self.log_file, "a+", encoding="utf-8") as file:
            file.write(f"{event.timestamp} - {event.event_type} at {event.source.__class__.__name__}\n")

        if "DEBUG" == "DEBUG": # TODO: Get configuration
            with open(self.log_long_file, "a+", encoding="utf-8") as file:
                file.write(f"{event.timestamp} - {event.event_type} at {event.source.__class__.__name__} throws:\n\t{event.data}\n\n")