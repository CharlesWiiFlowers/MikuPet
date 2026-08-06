import json
from tkinter import PhotoImage

from core.events.event_types import EVENT_ERROR, EVENT_METADATA_ASSET_LOADED
from core.events.event_bus import EventBus

class SpriteSheet:
    def __init__(self, bus:EventBus, image_path:str, metadata_path:str):
        self.bus = bus
        self.image_path = image_path
        self.metadata_path = metadata_path

        self.image = PhotoImage(file=self.image_path)
        self.metadata = None

        try:
            with open(self.metadata_path, "r", encoding="utf-8") as f:
                self.metadata = json.load(f)
                
        except (FileNotFoundError, json.JSONDecodeError) as e:
            self.bus.emit(
                event_name=EVENT_ERROR,
                source=self,
                data={"error": f"Failed to load metadata asset [{self.metadata_path}]: {str(e)}"}
            )

        self.frames = []

        self._split()

    def get_frames(self):
        self._split() # Ensure the frame is loaded

        return self.frames

    def _split(self):
        """
        Split the spritesheet into individual frames using LibreSprite metadata.
        """

        if self.metadata == None: return

        self.frames = []

        for frame_data in self.metadata["frames"].values():

            frame = frame_data["frame"]

            x = frame["x"]
            y = frame["y"]
            w = frame["w"]
            h = frame["h"]

            sprite = PhotoImage(width=w, height=h)

            sprite.tk.call(
                sprite,
                "copy",
                self.image,
                "-from",
                x,
                y,
                x + w,
                y + h,
                "-to",
                0,
                0
            )

            self.frames.append(sprite)