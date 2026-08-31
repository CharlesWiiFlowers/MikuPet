from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_UPDATE, WINDOW_STATE_UPDATED,EVENT_ERROR
from core.character import Character

class AutoWalk():
    def __init__(self, bus:EventBus, character: Character):
        self.bus = bus

        self.character = character

        self.current_window = None

        self.enableAutoWalk = True  # Flag to enable or disable auto walk

        # Register event listeners
        self.bus.on(ENGINE_UPDATE, self.update)

        self.bus.on(WINDOW_STATE_UPDATED, self._update_window_state)

    def update(self, event):
        self._verify_focus()
        self._apply_auto_walk()

    def _apply_auto_walk(self):

        if not self.enableAutoWalk:
            return
        
        if self.current_window is None:
            return  # No window information available yet

        right_limit = self.current_window["right"] - (self.character.width + 8)

        if (
            self.current_window["left"]
            <= self.character.position["x"]
            <= right_limit # TODO: Make this configurable. Replace 10 with renderer horizontal padding once exposed.
            ):
                self._emit_character_walking_animation_event_bus(isWalking=False)
                return # Character is within the window bounds, no need to auto walk
        
        # Apply auto walk
        new_position_on_x:float = self.character.position["x"]

        if self.character.position["x"] < self.current_window["left"]:
            new_position_on_x = self.character.position["x"] + 5  # Move right by 5 units. TODO: Make this configurable

            self._emit_character_walking_animation_event_bus()

        elif self.character.position["x"] > right_limit:
            new_position_on_x = self.character.position["x"] - 5 #, self.current_window["right"] - self.character.width) # TODO: Make this configurable

            self._emit_character_walking_animation_event_bus(isToRight=False)

        try:
            
            self.character.position["x"] = new_position_on_x

        except Exception as e:

            self.bus.emit(EVENT_ERROR, data={'error': str(e)})

    def _verify_focus(self):
        self.enableAutoWalk = not(self.character.has_focus)

    def _update_window_state(self, event):
        self.current_window = event.data

    def _emit_character_walking_animation_event_bus(
        self,
        isWalking=True,
        isToRight=True
    ):
    
        if self.character.is_doing_an_action:
            return
    
        if isWalking:
            self.character.change_animation(
                "walk_right" if isToRight else "walk_left"
            )
        else:
            self.character.change_animation("idle")