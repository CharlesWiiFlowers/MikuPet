"""
General settings for MikuPet. This file is used to store user preferences and configurations.
"""
from core.events.event_types import EVENT_CONFIG_LOADED, EVENT_ERROR, EVENT_CONFIG_UPDATE
from core.events.event_bus import EventBus
from core.file_system import FileSystem
from pathlib import Path
import json


class Config:

    DEFAULT_CONFIG = {
        "selected_character": "miku",
        "debug": True,
        "fps": 60,
        "random_actions": {
            "sneeze": {
                "min": 10,
                "max": 90
            }
        },
        "random_objects_spawn": {
            "leek": {
                "min": 20,
                "max": 200      
            }
        }
    }

    def __init__(self, bus: EventBus) -> None:
        self.bus = bus

        self.project_root = Path(__file__).resolve().parent.parent.parent

        self.config_dir = FileSystem.data()
        self.config_dir.mkdir(exist_ok=True)

        self.config_file = self.config_dir / "config.json"

        if not self.config_file.exists():
            self.data = self.DEFAULT_CONFIG.copy()
            self.save()
        else:
            try:
                with open(self.config_file, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.data = self.DEFAULT_CONFIG.copy()
                self.save()

                self.bus.emit(
                    event_name=EVENT_ERROR,
                    source=self,
                    data={"error": "Failed to load config. Using default settings."}
                )

        self._migrate_config()

    def save(self):
        with open(self.config_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)

    def get(self, key, default=None):
        return self.data.get(key, default)

    def set(self, key, value):
        self.data[key] = value

    def load(self):
        self.bus.emit(
            event_name=EVENT_CONFIG_LOADED,
            source=self
        )

    def _migrate_config(self):
        modified = False
        for key, value in self.DEFAULT_CONFIG.items():
            if key not in self.data:
                self.data[key] = value
                modified = True

        if modified:
            self.save()

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):

        if self.data.get(key) == value:
            return  # No change, do not emit event

        self.data[key] = value

        self.save()

        self.bus.emit(
            event_name=EVENT_CONFIG_UPDATE,
            source=self
        )