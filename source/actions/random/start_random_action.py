import random

from core.events.event_bus import EventBus
from core.events.event_types import ENGINE_PRE_UPDATE, ENGINE_UPDATE, EVENT_CONFIG_LOADED, EVENT_CONFIG_UPDATE
from core.character import Character


class RandomActions:
    def __init__(self, bus: EventBus, character: Character) -> None:
        self.bus = bus
        self.character = character
        self.config = {}

        self.elapsed_frames = 0

        self.next_action = None

        self.bus.on(
            ENGINE_PRE_UPDATE,
            self._verify
        )

        self.bus.on(
            ENGINE_UPDATE,
            self._update
        )

        self.bus.on(
            EVENT_CONFIG_LOADED,
            callback=self._load_config
        )

        self.bus.on(
            EVENT_CONFIG_UPDATE,
            callback=self._update_config
        )

    def _load_config(self, event):
        self.config = event.source

        self.fps = self.config["fps"]

        self.actions = {
            "sneeze": [self.config["random_actions"]["sneeze"], 0] # [{min time, max time}, seconds to next action]
        }

        self.objects = {
            "leek": [self.config["random_objects_spawn"]["leek"], 0] # [{min time, max time}, seconds to next spawn]
        }

    def _update_config(self, event):
            self._load_config(event=event)

    def _verify(self, event):
        self.elapsed_frames += 1

        self.next_action = None

        for x, _ in self.actions.items():
             action = self.actions[x]
             if action[1] <= 0:
                 self.next_action = x
                 action[1] = random.randint(action[0]["min"], action[0]["max"])

        for x, _ in self.objects.items():
             spawn = self.objects[x]
             if spawn[1] <= 0:
                 # TODO: Spawn Object
                 spawn[1] = random.randint(spawn[0]["min"], spawn[0]["max"])


        # A second has passed
        if (self.elapsed_frames % self.fps) == 0:
            for x, _ in self.actions.items():
                action = self.actions[x]
                action[1] -= 1

        if self.elapsed_frames > 100000 and (self.elapsed_frames % self.fps) == 0: self.elapsed_frames = 0 # To avoid large numbers

    def _update(self, event):
        if self.next_action is not None:
             self._start_random_action(action=self.next_action)

    def _start_random_action(self, action: str):

        print(
        "[ACTION START]",
        action,
        "is_doing:",
        self.character.is_doing_an_action
    )

        
        if self.character.is_doing_an_action: return

        self.character.is_doing_an_action = True
        self.character.change_animation(action)