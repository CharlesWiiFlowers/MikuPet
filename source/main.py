from core.events.event_bus import EventBus
from core.config import Config
from utils.logger import Logger

class Main():
    def __init__(self) -> None:
        self.bus = EventBus()

        self.config = Config(bus=self.bus)
        self.logger = Logger(bus=self.bus)

if __name__ == "__main__":
    Main()
