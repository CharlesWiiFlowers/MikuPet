from core.events.event_bus import EventBus
from core.events.event_types import EVENT_DRAG, EVENT_DRAG_END
from core.character import Character

class DragSystem():
    def __init__(self, bus: EventBus, character: Character) -> None:
        self.bus = bus
        self.character = character

        self.bus.on(
            EVENT_DRAG,
            self._on_drag
        )

        self.bus.on(
            EVENT_DRAG_END,
            self._no_drag
        )


    def _on_drag(self, event):

        if not self.character.has_focus:
            return

        self.character.position["x"] = (
            event.data["mouse_x"] - event.data["offset_x"]
        )

        self.character.position["y"] = (
            event.data["mouse_y"] - event.data["offset_y"]
        )

    def _no_drag(self, event):
        self.character.is_dragging = False

