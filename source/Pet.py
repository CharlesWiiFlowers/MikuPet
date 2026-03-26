<<<<<<< HEAD
"""This gonna be a hell to make again
        Days trying to make: infinity
        I always give up but I'll do"""

import os
import tkinter
import threading
import warnings
import json
from mod.sprites import Animation
from mod.actions import Actions
from mod.actions import AutoActions

class PetUI():
    def __init__(self, image_path) -> None:
        
        # Get all images
        self.image_path = image_path

class AppUI(tkinter.Tk):

    def __init__(self):
        # Initialize the main window
        super().__init__()

        character_selected = settings["selected_character"]
        if settings["selected_character"] not in CHARACTER_FOLDER:
            warnings.warn("[SYSTEM] Warning, selected character not found. Loading default.")
            character_selected = "miku"

        # Get all items on list dir
        IMAGE_PATH:list[str] = [item for item in os.listdir(f"./assets/") if ".png" in item]

        SPRITE_NUMBER_OF_FRAMES = [20, 8, 8, 8, 5, 3, 12, 9]

        self.sprite = Animation(IMAGE_PATH, SPRITE_NUMBER_OF_FRAMES)
        self.actions = Actions(self.sprite.canvas, self)
        self.auto_actions = AutoActions(self.sprite.canvas, self)

        # Configure the main window
        self.resizable(False, False)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        #self.attributes("-alpha", 0.5)  # Set transparency to 50%
        self.config(bg=self.sprite.BACKGROUND_COLOR)
        self.wm_attributes("-transparentcolor", self.sprite.BACKGROUND_COLOR)

        # Start the sprite animation
        self.sprite.animation()
        self.auto_actions.gravity()
        self.auto_actions.move_in_x()

    def stop(self):
        self.quit()

    def change_animation(self, animation:int = 0):
        """
        Change the current animation of the sprite.
        :param animation: The index of the animation to change to.
        """
        self.sprite.animation_list = animation

=======
"""This gonna be a hell to make again"""
>>>>>>> e7ebe8a ([🐳] Commit: Minor change)
