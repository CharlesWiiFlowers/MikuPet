import tkinter
from PIL import Image, ImageTk

class Sprite():
    def __init__(self, image_path:str = "./assets/miku_sprite_71x59.png", x:int = 59, y:int = 65, animation_speed:int = 200, background_color:str = "#96C8FA"):
        self.IMAGE_PATH = image_path
        self.x = x
        self.y = y
        self.ANIMATION_SPEED = animation_speed # in milliseconds
        self.frames = []
        self.current_frame = 0
        self.BACKGROUND_COLOR = background_color

    def sprite_sheet(self):
        self.canvas = tkinter.Canvas(width=self.x, height=self.y, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

        sprite_sheet = Image.open(self.IMAGE_PATH)

        for y in range(sprite_sheet.height // self.y):
            for x in range(sprite_sheet.width // self.x):
                frame = sprite_sheet.crop((x * self.x, y * self.y, (x + 1) * self.x, (y + 1) * self.y))
                self.frames.append(ImageTk.PhotoImage(frame))

        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.frames[self.current_frame])

class AppUI(tkinter.Tk):
    def __init__(self):
        # Initialize the main window
        super().__init__()
        self.sprite = Sprite()
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
        