import random

from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_PRE_UPDATE, ENGINE_UPDATE
from core.character import Character


class RandomActions:
    def __init__(self, bus: EventBus, character: Character) -> None:
        self.bus = bus
        self.character = character

        self.actions = ["sneeze"]  # TODO: Add auto-added actions when the project grows

        self.action_to_do = None
        self.do_an_action = False

        self.bus.on(
            ENGINE_PRE_UPDATE,
            self._verify
        )

        self.bus.on(
            ENGINE_UPDATE,
            self._update
        )

    def _verify(self, event):
        self.do_an_action = random.randint(0, 10000) >= 9999

        if self.do_an_action:
            self.action_to_do = random.choice(self.actions)

    def _update(self, event):
        if not self.do_an_action:
            return

        if not self.action_to_do:
            return

        self.character.is_doing_an_action = True
        self._start_random_action(self.action_to_do)

        # Prevent the same action from being started every frame.
        self.do_an_action = False

    def _start_random_action(self, action: str):
        self.character.change_animation(action)