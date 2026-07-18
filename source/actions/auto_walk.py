from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED, EVENT_POSITION_CHANGED, EVENT_ON_FOCUS, EVENT_FOCUS_LOST, EVENT_ERROR

class AutoWalk():
    def __init__(self, bus:EventBus):
        self.bus = bus

        self.current_window = None

        self.position = {'x': 0, 'y': 0}  # Initial character position

        self.enableAutoWalk = True  # Flag to enable or disable auto walk

        # Register event listeners
        self.bus.on(ENGINE_UPDATE, self.apply_auto_walk)

        self.bus.on(EVENT_POSITION_CHANGED, self.character_position)

        self.bus.on(WINDOW_STATE_UPDATED, self.update_window_state)

        self.bus.on(EVENT_ON_FOCUS, self.disable_auto_walk)
                    
        self.bus.on(EVENT_FOCUS_LOST, self.enable_auto_walk)


    def update_window_state(self, event):
        self.current_window = event.data

    def apply_auto_walk(self, event):

        if not self.enableAutoWalk:
            return
        
        if self.current_window is None:
            return  # No window information available yet
        
        if self.position['x'] < self.current_window['right'] and self.position['x'] > self.current_window['left']:
            return  # Character is within the window bounds, no need to auto walk

        # Apply auto walk

        new_position_on_x: float = self.position['x'] + 5  # Move right by 5 units. TODO: Make this configurable

        if new_position_on_x > self.current_window['right']:
            new_position_on_x = self.current_window['right']
    
        try:
            self.bus.emit(EVENT_POSITION_CHANGED, data={'x': new_position_on_x, 'y': self.position['y']}, source=self) # pyright: ignore[reportPossiblyUnboundVariable]

        except Exception as e:

            self.bus.emit(EVENT_ERROR, data={'error': str(e)})

    def disable_auto_walk(self, event):
        self.enableAutoWalk = False

    def enable_auto_walk(self, event):
        self.enableAutoWalk = True

    def character_position(self, event):
        self.position = event.data