from core.events.event_bus import EventBus
from core.events.event_types import (
    EVENT_CHARACTER_ANIMATION_CHANGED,
    EVENT_ASSET_LOADED,
    ENGINE_RENDER,
    EVENT_SPRITE_FRAME_CHANGED,
    EVENT_CONFIG_LOADED,
    EVENT_ON_PADDING_CHANGE
)
from core.character import Character
from render.sprite import Sprite
from render.sprite_sheet import SpriteSheet


class Animation:
    def __init__(
        self,
        bus: EventBus,
        sprite: Sprite,
        character: Character
    ) -> None:

        self.bus = bus

        self.config = {}

        self.sprite = sprite
        self.character = character

        self.animations = {}

        self.current_animation_vector = []
        self.current_animation_frame = 0

        self.frame = 0
        self.passed_frames_in_animation = 0

        self.delta_time = 0.1666
        self.animation_timer = 0

        self.animation_padding = [10, 10]

        self.bus.on(
            EVENT_CONFIG_LOADED,
            self._load_config
        )

        self.bus.on(
            EVENT_ASSET_LOADED,
            self._load_assets
        )

        self.bus.on(
            EVENT_CHARACTER_ANIMATION_CHANGED,
            self.change_character_animation
        )

        self.bus.on(
            ENGINE_RENDER,
            self._tick
        )

        self._load_vector_frame()

    def change_character_animation(self, event):
        self.current_animation_frame = 0
        self.passed_frames_in_animation = 0
        self.animation_timer = 0

        self._load_vector_frame()

    def _load_config(self, event):
        self.config = event.source

        self.delta_time = 1 / self.config["fps"]

    def _load_vector_frame(self):
        if not self.animations:
            return

        animation_name = self.character.animation_name

        if animation_name not in self.animations:
            return

        self.current_animation_vector = (
            self.animations[animation_name].frames
        )

    def _continue_frame_animation(self):
        if not self.current_animation_vector:
            return

        if self.current_animation_frame < len(self.current_animation_vector) - 1:
            self.current_animation_frame += 1
        else:
            self.current_animation_frame = 0
            self.passed_frames_in_animation += 1

    def _load_assets(self, event):
        self.animations: dict[str, SpriteSheet] = event.data

        self._load_vector_frame()

    def _verify_padding(self):
        x, y = self.sprite.get_padding(
            self.character.animation_name
        )

        if [x, y] == self.animation_padding:
            return

        self.animation_padding = [x, y]

        self.bus.emit(
            EVENT_ON_PADDING_CHANGE,
            self.animation_padding,
            self
        )

    def _tick(self, event):

        # Engine
        self.frame += 1

        if not self.current_animation_vector:
            return

        self._verify_padding()

        # Animation
        self.animation_timer += self.delta_time

        animation_fps = self.sprite.get_animation_fps(
            self.character.animation_name
        )

        if animation_fps is None:
            animation_fps = 8

        frame_duration = 1 / animation_fps

        if self.animation_timer >= frame_duration:

            self._continue_frame_animation()
            self.animation_timer = 0

            loop_count = self.sprite.get_animation_frame_loop_count(
                self.character.animation_name
            )

            if loop_count is not None and loop_count != -1:

                if self.passed_frames_in_animation >= loop_count:

                    print(
                        "[ACTION END]",
                        self.character.animation_name,
                        "passed:",
                        self.passed_frames_in_animation,
                        "loop:",
                        loop_count
                    )

                    self.character.change_animation("idle")

                    self.character.is_doing_an_action = False

        self.bus.emit(
            event_name=EVENT_SPRITE_FRAME_CHANGED,
            source=self,
            data=self.current_animation_vector[
                self.current_animation_frame
            ]
        )