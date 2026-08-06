from core.events.event_bus import EventBus
from core.events.event_types import MONITORS_UPDATED, ENGINE_PRE_UPDATE, MONITOR_CHANGED
from systems.monitor_info import MonitorInfo
from systems.platform.Windows.get_monitors import get_monitors

class MonitorSystem:

    def __init__(self, bus: EventBus):

        self.bus = bus

        self.monitors = []

        self.current_monitor = None

        self.load_monitors()


    def load_monitors(self):

        self.monitors = get_monitors()

        self.bus.emit(
            event_name=MONITORS_UPDATED,
            data=self.monitors,
            source=self
        )


# TODO: Move this class to another place!!!

