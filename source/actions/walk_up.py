from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED
from core.character import Character

class WalkUp():
    def __init__(self, bus:EventBus, character:Character) -> None:
        self.bus = bus
        self.character = character

        self.current_window = None

        self.bus.on(ENGINE_UPDATE, self._apply_walk_up)
        self.bus.on(WINDOW_STATE_UPDATED, self._update_window_state)

    def _apply_walk_up(self, event):
        if self.current_window is None: return

        if self.character.position["y"] - self.character.height >= self.current_window["bottom"]: return

        # Apply walk up
        self.character.position["y"] += 5 # TODO: Make this configurable
    
    def _update_window_state(self, event):
        self.current_window = event.data
