from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED, EVENT_POSITION_CHANGED, EVENT_ON_FOCUS, EVENT_FOCUS_LOST, EVENT_ERROR

class Gravity():
    def __init__(self, bus:EventBus):
        self.bus = bus

        self.current_window = None

        self.position = {'x': 0, 'y': 0}  # Initial character position

        self.gravity_strength = 9.81  # Default gravity strength in m/s^2

        self.enableGravity = True  # Flag to enable or disable gravity

        # Register event listeners
        self.bus.on(ENGINE_UPDATE, self.apply_gravity)

        self.bus.on(EVENT_POSITION_CHANGED, self.character_position)

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
        
        if self.position['y'] < self.current_window['bottom']:
            # Apply gravity
            new_position_on_y: float = self.position['y'] + self.gravity_strength * 0.016  # Assuming 60 FPS, so delta time is ~0.016 seconds. TODO: Make this configurable

            if new_position_on_y > self.current_window['bottom']:
                new_position_on_y = self.current_window['bottom']
        
        try:
            self.bus.emit(EVENT_POSITION_CHANGED, data={'x': self.position['x'], 'y': new_position_on_y}) # pyright: ignore[reportPossiblyUnboundVariable]
        except Exception as e:
            self.bus.emit(EVENT_ERROR, data={'error': str(e)})

    def disable_gravity(self, event):
        self.enableGravity = False

    def enable_gravity(self, event):
        self.enableGravity = True

    def character_position(self, event):
        self.position = event.data
