"""
Load spritesheets and their metadata.
"""

import json
from pathlib import Path

from core.events.event_bus import EventBus
from core.events.event_types import (
    EVENT_ERROR,
    EVENT_CONFIG_LOADED,
    EVENT_ASSET_LOADED,
    EVENT_METADATA_ASSET_LOADED
)

from render.sprite_sheet import SpriteSheet


class AssetLoader:

    def __init__(self, bus: EventBus):

        self.bus = bus

        self.config = None

        self.sheet: dict[str, SpriteSheet] = {}

        self.bus.on(
            EVENT_CONFIG_LOADED,
            self._on_config_loaded
        )


    def load_character_assets(self):

        if self.config is None:

            self.bus.emit(
                EVENT_ERROR,
                source=self,
                data={
                    "error": "Config not loaded."
                }
            )
            return

        selected_character = self.config.get(
            "selected_character",
            "miku"
        )

        character_dir = Path(
            "assets",
            "characters",
            selected_character
        )

        character_file = character_dir / "character.json"

        try:

            with character_file.open(
                "r",
                encoding="utf-8"
            ) as f:

                character_data = json.load(f)

        except (FileNotFoundError, json.JSONDecodeError) as e:

            self.bus.emit(
                EVENT_ERROR,
                source=self,
                data={
                    "error": f"Failed to load character assets: {e}"
                }
            )
            return

        self.sheet.clear()

        self.bus.emit(
            EVENT_METADATA_ASSET_LOADED,
            source=self,
            data=character_data
        )

        self._load_animations(
            character_dir,
            character_data
        )

        self.bus.emit(
            EVENT_ASSET_LOADED,
            source=self,
            data=self.sheet
        )


    def _load_animations(
        self,
        sprites_path: Path,
        character_metadata: dict
    ):

        for animation_name, animation in character_metadata["animations"].items():

            self.sheet[animation_name] = SpriteSheet(

                self.bus,

                sprites_path / animation["file"],

                sprites_path / animation["metadata"]

            )


    def _on_config_loaded(self, event):

        self.config = event.source

        self.load_character_assets()