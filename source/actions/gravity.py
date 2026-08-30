from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED, EVENT_ERROR, ENGINE_PRE_UPDATE
from core.character import Character

class Gravity():
    def __init__(self, bus:EventBus, character: Character):
        self.bus = bus
        self.character = character

        self.current_window = None

        self.gravity_strength = 10  # Default gravity strength in m/s^2

        self.enableGravity = True  # Flag to enable or disable gravity

        self.frames_to_wait = 0

        # Register event listeners
        self.bus.on(ENGINE_PRE_UPDATE, self.pre_update)

        self.bus.on(ENGINE_UPDATE, self.update)

        self.bus.on(WINDOW_STATE_UPDATED, self._update_window_state)

    def pre_update(self, event):
        self._verify_focus()

    def update(self, event):
        if self.frames_to_wait <= 0:
            self._apply_gravity()
        else:
            self.frames_to_wait -= 1

    def _update_window_state(self, event):
        self.current_window = event.data

        self.frames_to_wait = 5

    def _apply_gravity(self):

        if not self.enableGravity:
            return
        
        if self.current_window is None:
            return  # No window information available yet
        
        if self.character.position["y"] < self.current_window['bottom']:
            ground = self.current_window["bottom"] - 100 # TODO: Adapt to real height of sprites

            # Apply gravity
            if self.character.position["y"] == 0: 
                self.character.position["y"] = 1  # Set a small initial value to avoid zero multiplication

            new_position_on_y: float = self.character.position["y"] + self.gravity_strength #TODO: Make this configurable

            if new_position_on_y > ground:
                new_position_on_y = ground
        
            try:
                self.character.position["y"] = float(new_position_on_y)

            except Exception as e:
                self.bus.emit(EVENT_ERROR, data={'error': str(e)})


    def _verify_focus(self):
        self.enableGravity = not(self.character.has_focus)