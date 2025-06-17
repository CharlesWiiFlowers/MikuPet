import tkinter
from PIL import Image, ImageTk

class Sprite():
    def __init__(self, image_path:list[str], x:int = 59, y:int = 65, animation_speed:int = 300, background_color:str = "#96C8FA"):
        self.IMAGE_PATH = image_path
        self.x = x
        self.y = y
        self.frames_axis = []
        self.ANIMATION_SPEED = animation_speed # in milliseconds
        self.frames = []
        self.waiting_animation_frames = []
        self.current_frame = 0
        self.BACKGROUND_COLOR = background_color
        self.canvas = tkinter.Canvas(width=self.x, height=self.y, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

    def update_animation_frames(self):
        # Add to waiting_animation_frames
        for i in range(21, len(self.frames)-1):
            print(self.frames[i])
            self.waiting_animation_frames.append(self.frames[i])

    def sprite_sheet(self):
        # Load the sprite sheet image
        sprite_sheet = []
        for i in range(len(self.IMAGE_PATH)):
            if i != 0 and i != 2:
                sprite_sheet.append(Image.open(self.IMAGE_PATH[i]))

        for i in range(len(sprite_sheet)):
            self.frames_axis.append((sprite_sheet[i].width, sprite_sheet[i].height))
            for x in range(sprite_sheet[i].width // self.x):
                frame = sprite_sheet[i].crop((x * self.x, 0, (x + 1) * self.x, sprite_sheet[i].height))
                self.frames.append(ImageTk.PhotoImage(frame))

        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.frames[self.current_frame])
        self.update_animation_frames()
        self.waiting_animation()

    def waiting_animation(self):
        self.current_frame = (self.current_frame + 1) % len(self.waiting_animation_frames)
        self.canvas.config(width=self.frames_axis[self.current_frame][0], height=self.frames_axis[self.current_frame][1])
        self.canvas.itemconfig(self.canvas.find_all()[0], image=self.waiting_animation_frames[self.current_frame])
        self.canvas.after(self.ANIMATION_SPEED, self.waiting_animation)