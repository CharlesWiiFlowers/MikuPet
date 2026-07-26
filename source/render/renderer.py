import tkinter as tk

from core.events.event_bus import EventBus
from core.events.event_types import (
    EVENT_POSITION_CHANGED,
    EVENT_SPRITE_FRAME_CHANGED,
    EVENT_ON_PADDING_CHANGE,
    ENGINE_RENDER
)


class Renderer:

    def __init__(self, bus: EventBus):

        self.bus = bus

        self.root = tk.Tk()

        self.frame_padding = [10, 10]

        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)

        self.root.configure(bg="#96C8FA")
        self.root.wm_attributes("-transparentcolor", "#96C8FA")

        self.canvas = tk.Canvas(
            self.root,
            bg="#96C8FA",
            highlightthickness=0
        )
        self.canvas.pack()

        self.current_frame = None

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

        self.bus.on(
            EVENT_ON_PADDING_CHANGE,
            self._on_padding_changed
        )

    def _on_padding_changed(self, event):
        self.frame_padding = event.data

    def _on_position_changed(self, event):

        self.x = event.data["x"]
        self.y = event.data["y"]

    def _on_sprite_changed(self, event):

        self.current_frame = event.data

    def _on_render(self, event):

        if self.current_frame is None:
            return

        self.canvas.itemconfig(
            self.sprite_id,
            image=self.current_frame
        )

        width = self.current_frame.width()
        height = self.current_frame.height()

        self.canvas.config(
            width=width,
            height=height
        )

        # self.frame_padding[0]
        # self.frame_padding[1]

        self.root.geometry(
            f"{int(width)}x{int(height)}+{int(self.x+self.frame_padding[0])}+{int(self.y-self.frame_padding[1])}"
        )

        try:
            self.root.update()
        except tk.TclError:
            pass