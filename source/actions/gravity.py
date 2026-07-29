from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED, EVENT_ON_FOCUS, EVENT_FOCUS_LOST, EVENT_ERROR
from core.character import Character

class Gravity():
    def __init__(self, bus:EventBus, character: Character):
        self.bus = bus
        self.character = character

        self.current_window = None

        self.gravity_strength = 10  # Default gravity strength in m/s^2

        self.enableGravity = True  # Flag to enable or disable gravity

        # Register event listeners
        self.bus.on(ENGINE_UPDATE, self.apply_gravity)

        self.bus.on(WINDOW_STATE_UPDATED, self.update_window_state)

        self.bus.on(EVENT_ON_FOCUS, self.disable_gravity)
                    
        self.bus.on(EVENT_FOCUS_LOST, self.enable_gravity)


    def update_window_state(self, event):
        self.current_window = event.data

    def apply_gravity(self, event):

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

    def disable_gravity(self, event):
        self.enableGravity = False

    def enable_gravity(self, event):
        self.enableGravity = True

    def character_position(self, event):
        self.position = event.data
