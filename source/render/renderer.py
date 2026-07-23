import tkinter as tk

from core.events.event_bus import EventBus
from core.events.event_types import (
    EVENT_POSITION_CHANGED,
    EVENT_SPRITE_FRAME_CHANGED,
    ENGINE_RENDER
)


class Renderer:

    def __init__(self, bus: EventBus):

        self.bus = bus

        self.root = tk.Tk()

        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.root.configure(
            bg="#96C8FA"
        )

        self.root.wm_attributes(
            "-transparentcolor",
            "#96C8FA"
        )


        self.canvas = tk.Canvas(
            self.root,
            bg="#96C8FA",
            highlightthickness=0
        )

        self.canvas.pack()


        self.image = None

        self.sprite_id = self.canvas.create_image(
            0,
            0,
            anchor=tk.NW
        )


        self.x = 0
        self.y = 0


        self.bus.on(
            EVENT_POSITION_CHANGED,
            self._on_position_changed
        )


        self.bus.on(
            EVENT_SPRITE_FRAME_CHANGED,
            self._on_sprite_changed
        )

        self.bus.on(
            ENGINE_RENDER,
            self._on_render
        )


    def _on_render(self, event):

        self.root.update_idletasks()
        self.root.update()

    def _on_position_changed(self, event):

        self.x = event.data["x"]
        self.y = event.data["y"]

        self.root.geometry(
            f"+{self.x}+{self.y}"
        )


    def _on_sprite_changed(self, event):

        self.image = event.data

        self.canvas.itemconfig(
            self.sprite_id,
            image=self.image
        )