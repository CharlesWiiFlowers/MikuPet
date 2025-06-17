import tkinter
from mod.sprites import Sprite
from mod.actions import Actions

class AppUI(tkinter.Tk):

    def __init__(self):
        # Initialize the main window
        super().__init__()

        IMAGE_PATH = ["./assets/miku_sprite_sheet_original.png",
                  "./assets/miku_sprite_sheet_1.png",
                  "./assets/miku_sprite_sheet_2.png",
                  "./assets/miku_sprite_sheet_3.png",
                  "./assets/miku_sprite_sheet_4.png",
                  "./assets/miku_sprite_sheet_5.png",
                  "./assets/miku_sprite_sheet_6.png",
                  "./assets/miku_sprite_sheet_7.png",
                  ]


        self.sprite = Sprite(IMAGE_PATH)
        self.actions = Actions(self.sprite.canvas, self)
        self.resizable(False, False)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        #self.attributes("-alpha", 0.5)  # Set transparency to 50%
        self.config(bg=self.sprite.BACKGROUND_COLOR)
        self.wm_attributes("-transparentcolor", self.sprite.BACKGROUND_COLOR)
        self.sprite.sprite_sheet()


if __name__ == "__main__":
    # Create the main window
    AppUI().mainloop()
        