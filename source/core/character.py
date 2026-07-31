from core.events.event_bus import EventBus
from core.events.event_types import EVENT_SPRITE_FRAME_CHANGED, EVENT_CHARACTER_ANIMATION_CHANGED

class Character():
    def __init__(self, bus:EventBus) -> None:
        self.bus = bus

        self.position: dict[str, float] = {"x": 0, "y": 0}
        self.width = 0
        self.height = 0

        self.has_focus = False
        self.is_dragging = False
        self.animation_name = "idle"

        self.bus.on(
            EVENT_SPRITE_FRAME_CHANGED,
            self._on_sprite_changed
        )

    def change_animation(self, animation_name:str):
        if self.animation_name == animation_name: return

        self.animation_name = animation_name

        self.bus.emit(
            EVENT_CHARACTER_ANIMATION_CHANGED,
            source=self
        )

    def _on_sprite_changed(self, event):
        self.width = event.data.width()
        self.height = event.data.height()