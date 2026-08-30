from core.events.event_bus import EventBus
from core.events.event_types import EVENT_SPRITE_FRAME_CHANGED, EVENT_CHARACTER_ANIMATION_CHANGED, ENGINE_PRE_UPDATE, EVENT_ON_FOCUS, EVENT_FOCUS_LOST

class Character():
    def __init__(self, bus:EventBus, pid:int) -> None:
        self.bus = bus

        self.PID = pid

        self.position: dict[str, float] = {"x": 0, "y": 0}
        self.width = 0
        self.height = 0

        self.has_focus = False
        self.is_dragging = False
        self.animation_name = "idle"
        self.is_doing_an_action = False

        self.bus.on(
            EVENT_SPRITE_FRAME_CHANGED,
            self._on_sprite_changed
        )

        self.bus.on(
            ENGINE_PRE_UPDATE,
            self._pre_update
        )

    def change_animation(self, animation_name:str):
        if self.animation_name == animation_name: return

        self.animation_name = animation_name

        self.bus.emit(
            EVENT_CHARACTER_ANIMATION_CHANGED,
            source=self
        )

    def _pre_update(self, event):
        if self.has_focus: self.change_animation("dragging")

    def _on_sprite_changed(self, event):
        self.width = event.data.width()
        self.height = event.data.height()

    def set_focus(self, enable:bool=True):
        self.has_focus = enable

        self.bus.emit(
            EVENT_ON_FOCUS if self.has_focus else EVENT_FOCUS_LOST,
            source=self
        )

    def get_PID(self):
        return self.PID