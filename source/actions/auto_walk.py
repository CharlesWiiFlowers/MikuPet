from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED, EVENT_ON_FOCUS, EVENT_FOCUS_LOST, EVENT_ERROR, EVENT_CHARACTER_ANIMATION_CHANGED, EVENT_WALKING_RIGHT
from core.character import Character

class AutoWalk():
    def __init__(self, bus:EventBus, character: Character):
        self.bus = bus

        self.character = character

        self.current_window = None

        self.enableAutoWalk = True  # Flag to enable or disable auto walk

        # Register event listeners
        self.bus.on(ENGINE_UPDATE, self._apply_auto_walk)

        self.bus.on(WINDOW_STATE_UPDATED, self._update_window_state)

        self.bus.on(EVENT_ON_FOCUS, self._disable_auto_walk)
                    
        self.bus.on(EVENT_FOCUS_LOST, self._enable_auto_walk)


    def _apply_auto_walk(self, event):

        if not self.enableAutoWalk:
            return
        
        if self.current_window is None:
            return  # No window information available yet
        
        if self.character.position["x"] < self.current_window['right'] and self.character.position["x"] > self.current_window['left']:
            self._emit_character_walking_animation_event_bus(isWalking=False)

            return  # Character is within the window bounds, no need to auto walk

        # Apply auto walk
        new_position_on_x:float = self.character.position["x"]

        if self.character.position["x"] < self.current_window["left"]:
            new_position_on_x = min(self.character.position["x"] + 5, self.current_window["left"])  # Move right by 5 units. TODO: Make this configurable

            self._emit_character_walking_animation_event_bus()

        if self.character.position["x"] > self.current_window["right"]:
            new_position_on_x = max(self.character.position["x"] - 5, self.current_window["right"]) # TODO: Make this configurable

            self._emit_character_walking_animation_event_bus(isToRight=False)

        try:
            
            self.character.position["x"] = new_position_on_x

        except Exception as e:

            self.bus.emit(EVENT_ERROR, data={'error': str(e)})

    def _update_window_state(self, event):
        self.current_window = event.data

    def _disable_auto_walk(self, event):
        self.enableAutoWalk = False

    def _enable_auto_walk(self, event):
        self.enableAutoWalk = True

    def _emit_character_walking_animation_event_bus(self, isWalking=True, isToRight=True):
        if isWalking:
            self.bus.emit(
                EVENT_CHARACTER_ANIMATION_CHANGED,
                ("walk_right" if isToRight else "walk_left"),
                source=self
            )
        else:
            self.bus.emit(
                event_name=EVENT_CHARACTER_ANIMATION_CHANGED,
                data="idle",
                source=self
            )