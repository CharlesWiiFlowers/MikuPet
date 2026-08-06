from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED
from core.character import Character

class WalkUp():
    def __init__(self, bus:EventBus, character:Character) -> None:
        self.bus = bus
        self.character = character

        self.current_window = None
        self.enable_walk_up = True

        # TODO: Add PRE_UPDATE Verifying

        self.bus.on(ENGINE_UPDATE, self.update)
        self.bus.on(WINDOW_STATE_UPDATED, self._update_window_state)

    def update(self, event):
        self._verify_focus()
        self._apply_walk_up()

    def _apply_walk_up(self):

        if self.enable_walk_up is False: return

        if self.current_window is None: return

        if self.character.position["y"] + self.character.height <= self.current_window["bottom"]: return

        # Apply walk up
        self.character.position["y"] -= 5 # TODO: Make this configurable
    
    def _update_window_state(self, event):
        self.current_window = event.data

    def _verify_focus(self):
        self.enable_walk_up = not(self.character.has_focus)