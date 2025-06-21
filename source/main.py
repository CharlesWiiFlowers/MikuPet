import tkinter
import json
from mod.sprites import Sprite
from mod.actions import Actions
from mod.actions import AutoActions

class AppUI(tkinter.Tk):

    def __init__(self):
        # Initialize the main window
        super().__init__()

        IMAGE_PATH = [
                  "./assets/miku_sprite_sheet_1.png",
                  "./assets/miku_sprite_sheet_2.png",
                  "./assets/miku_sprite_sheet_3.png",
                  "./assets/miku_sprite_sheet_4.png",
                  "./assets/miku_sprite_sheet_5.png",
                  "./assets/miku_sprite_sheet_6.png",
                  "./assets/miku_sprite_sheet_7.png",
                  ]

        SPRITE_NUMBER_OF_FRAMES = [20, 8, 9, 8, 5, 3, 12]

        self.sprite = Sprite(IMAGE_PATH, SPRITE_NUMBER_OF_FRAMES)
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
        self.sprite.sprite_sheet()
        self.auto_actions.gravity()


if __name__ == "__main__":
    # Create the main window
    AppUI().mainloop()
        