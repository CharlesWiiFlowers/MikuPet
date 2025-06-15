import tkinter
from PIL import Image, ImageTk

class Sprite():
    def __init__(self, image_path:str = "./assets/miku_sprite_71x59.png", x:int = 59, y:int = 65, animation_speed:int = 200):
        self.IMAGE_PATH = image_path
        self.x = x
        self.y = y
        self.ANIMATION_SPEED = animation_speed # in milliseconds
        self.frames = []
        self.current_frame = 0

    def sprite_sheet(self):
        self.canvas = tkinter.Canvas(width=self.x, height=self.y)
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
        self.resizable(False, False)
        self.overrideredirect(True)
        self.attributes("-topmost", True)
        self.sprite = Sprite()
        self.sprite.sprite_sheet()


if __name__ == "__main__":
    # Create the main window
    AppUI().mainloop()
        