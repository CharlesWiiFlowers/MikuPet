"""
Load Spritesheets and their metadata.
"""
import json

from core.events.event_bus import EventBus
from core.events.event_types import EVENT_ERROR, EVENT_CONFIG_LOADED, EVENT_ASSET_LOADED, EVENT_METADATA_ASSET_LOADED
from render.sprite_sheet import SpriteSheet

class AssetLoader:
    def __init__(self, bus: EventBus) -> None:
        self.bus = bus
        self.config = None
        self.sheet = {}

        self.bus.on(event_name=EVENT_CONFIG_LOADED, callback=self._on_config_loaded)

    def load_character_assets(self):
        if not self.config:
            self.bus.emit(
                event_name=EVENT_ERROR,
                source=self,
                data={"error": "Config not loaded. Cannot load character assets."}
            )
            return

        
        selected_character = self.config
        general_sprite_path = f"assets/characters/{selected_character}"
        character_path = f"{general_sprite_path}/character.json"

        try:
            with open(character_path, "r", encoding="utf-8") as f:
                character_data = json.load(f)

                self.bus.emit(
                    event_name=EVENT_METADATA_ASSET_LOADED,
                    source=self,
                    data=character_data
                )


                # TODO: Add a default texture to use as placeholder for missing animations
                self._load_animations(general_sprite_path, character_data)

                self.bus.emit(
                    event_name=EVENT_ASSET_LOADED,
                    source=self,
                    data=self.sheet
                )

                
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.bus.emit(
                event_name=EVENT_ERROR,
                source=self,
                data={"error": f"Failed to load character assets: {str(e)}"}
            )

    def _load_animations(self, sprites_path:str, character_metadata: dict):

        for animation_name, value in character_metadata["animations"].items():
            self.sheet[animation_name] = SpriteSheet(self.bus, f'{sprites_path}/{value["file"]}', f'{sprites_path}/{value["metadata"]}') # TODO: Use Pathlib

    def _on_config_loaded(self, event):
        self.config = event.source

        self.load_character_assets()
