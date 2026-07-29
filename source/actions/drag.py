from core.events.event_bus import EventBus
from core.events.event_types import EVENT_DRAG
from core.character import Character

class DragSystem():
    def __init__(self, bus: EventBus, character: Character) -> None:
        self.bus = bus
        self.character = character

        self.bus.on(
            EVENT_DRAG,
            self._on_drag
        )


    def _on_drag(self, event):
        x = event.data["mouse_x"] - event.data["offset_x"]
        y = event.data["mouse_y"] - event.data["offset_y"]

        self.character = {"x": x, "y": y}

