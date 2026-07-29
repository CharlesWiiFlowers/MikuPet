from core.events.event_bus import EventBus
from core.character import Character
from core.config import Config
from core.engine import Engine
from render.animation import Animation
from render.asset_loader import AssetLoader
from render.renderer import Renderer
from render.sprite import Sprite
from systems.window_system import WindowSystem
from actions.gravity import Gravity
from actions.auto_walk import AutoWalk
from utils.logger import Logger

class Main():
    def __init__(self) -> None:

        # Initialize core components
        self.bus = EventBus()
        self.character = Character()
        self.config = Config(bus=self.bus)
        self.logger = Logger(bus=self.bus)
        self.engine = Engine(bus=self.bus)

        # Initialize systems
        self.window_system = WindowSystem(bus=self.bus)

        # Initialize actions
        self.gravity = Gravity(bus=self.bus, character=self.character)
        self.auto_walk = AutoWalk(bus=self.bus, character=self.character)

        # Initialize Render
        self.asset_loader = AssetLoader(bus=self.bus)
        self.sprite = Sprite(bus=self.bus)
        self.animation = Animation(bus=self.bus, sprite=self.sprite)
        self.render = Renderer(bus=self.bus, character=self.character)

        self.config.load()
        self.engine.start()

if __name__ == "__main__":
    Main()
