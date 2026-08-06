from core.events.event_bus import EventBus
from core.events.event_types import EVENT_ASSET_LOADED, EVENT_METADATA_ASSET_LOADED, EVENT_ERROR

class Sprite():
    def __init__(self, bus:EventBus) -> None:
        self.bus = bus

        self.on_focus = False        
        self.sprites = None
        self.character_metadata = None

        self.default_x_padding = 10
        self.default_y_padding = 10 # TODO: Make this configurable

        self.bus.on(
            event_name=EVENT_ASSET_LOADED,
            callback=self._load_animation_assets
        )

        self.bus.on(
            event_name=EVENT_METADATA_ASSET_LOADED,
            callback=self._load_character_metadata
        )

    def get_animation_fps(self, animation:str):
        if self.character_metadata is None: return

        return self.character_metadata["animations"][animation]["fps"]

    def get_padding(self, animation:str):
        if self.character_metadata is None: return self.default_x_padding, self.default_y_padding

        try:
            return self.character_metadata["animations"][animation]["padding"][0], self.character_metadata["animations"][animation]["padding"][1]
        except KeyError:

            self.bus.emit(
                EVENT_ERROR,
                data=f"Missing specific padding for {animation}"
            )

            return self.default_x_padding, self.default_y_padding

    def _load_animation_assets(self, event):
        self.sprites = event.data

    def _load_character_metadata(self, event):
        self.character_metadata = event.data