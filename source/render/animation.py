from core.events.event_bus import EventBus
from core.events.event_types import EVENT_CHARACTER_ANIMATION_CHANGED, EVENT_ASSET_LOADED, ENGINE_RENDER, EVENT_SPRITE_FRAME_CHANGED, EVENT_CONFIG_LOADED
from render.sprite import Sprite
from render.sprite_sheet import SpriteSheet

class Animation():
    def __init__(self, bus: EventBus, sprite: Sprite) -> None:
        self.bus = bus

        self.config = {}

        self.character = sprite

        self.animations = {}

        self.current_animation = "idle"

        self.current_animation_vector = []

        self.current_animation_frame = 0

        self.frame = 0

        self.delta_time = 0.1666

        self.animation_timer = 0

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
        self.current_animation = event.data

    def _load_config(self, event):
        self.config = event.source

        self.delta_time = 1 / self.config["fps"]

    def _load_vector_frame(self):
        if self.animations == {}:
            return
        else:
            self.current_animation_vector = self.animations[self.current_animation].frames

    def _continue_frame_animation(self):
         if self.current_animation_vector != []:
            self.current_animation_frame = self.current_animation_frame + 1 if (len(self.current_animation_vector) -1 > self.current_animation_frame) else 0



    def _load_assets(self,event):
        self.animations: dict[str, SpriteSheet] = event.data

        self._load_vector_frame()

    def _tick(self, event):
            self.frame += 1

            self.animation_timer += self.delta_time

            animation_fps = 1/8 if self.character.get_animation_fps(self.current_animation) is None else (1 / self.character.get_animation_fps(self.current_animation)) # type: ignore

            if self.animation_timer >= (animation_fps):

                self._continue_frame_animation()
                self.animation_timer = 0

            if self.current_animation_vector:
                self.bus.emit(
                event_name=EVENT_SPRITE_FRAME_CHANGED,
                source=self,
                data=self.current_animation_vector[self.current_animation_frame]
            )