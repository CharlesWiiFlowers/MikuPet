from core.events.event_bus import EventBus
from core.config import Config
from core.engine import Engine
from systems.window_system import WindowSystem
from actions.gravity import Gravity
from utils.logger import Logger

class Main():
    def __init__(self) -> None:
        self.bus = EventBus()

        # Initialize core components
        self.config = Config(bus=self.bus)
        self.logger = Logger(bus=self.bus)
        self.engine = Engine(bus=self.bus)

        # Initialize systems
        self.window_system = WindowSystem(bus=self.bus)

        # Initialize actions
        self.gravity = Gravity(bus=self.bus)

if __name__ == "__main__":
    Main()
