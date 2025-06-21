import tkinter
import warnings
from PIL import Image, ImageTk

class Sprite():
    def __init__(self, image_path:list[str], sprite_number_of, initial_x = 59, initial_y = 100, animation_speed:int = 100, background_color:str = "#96C8FA"):
        self.IMAGE_PATH = image_path
        self.SPRITE_NUMBER = sprite_number_of
        self.ANIMATION_SPEED = animation_speed # in milliseconds, less is faster
        
        # Every frames here
        self.frames = []
        self.frames_width = []
        self.y = initial_y # This don't change
        
        # List to hold frames for animation
        self.waiting_animation_frames = []

        self.current_frame = 0
        self.BACKGROUND_COLOR = background_color
        self.canvas = tkinter.Canvas(width=initial_x, height=self.y, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

    def update_animation_frames(self):
        # Add to waiting_animation_frames
        for i in range(0, 19):
            self.waiting_animation_frames.append(self.frames[i])

    def sprite_sheet(self):
        # Load the sprite sheet image
        sprite_sheet = []
        for i in range(0, len(self.IMAGE_PATH) -1):
            sprite_sheet.append(Image.open(self.IMAGE_PATH[i]))

        for i in range(len(sprite_sheet)-1):
            # Calculate the width of each frame based on the number of frames
            self.frames_width.append(sprite_sheet[i].width // self.SPRITE_NUMBER[i])
            
            if sprite_sheet[i].height != self.y:
                # If the height of the sprite sheet is not equal to the initial height, warn the user
                warnings.warn(f"The height of the sprite sheet {self.IMAGE_PATH[i]} is not equal to the initial height {self.y}. This may cause display issues.", UserWarning)

            for x in range(self.SPRITE_NUMBER[i]-1):
                # Crop the sprite sheet to get each frame
                frame = sprite_sheet[i].crop((x * self.frames_width[i], 0, (x + 1) * self.frames_width[i], sprite_sheet[i].height))
                self.frames.append(ImageTk.PhotoImage(frame))

        self.canvas.create_image(0, 0, anchor=tkinter.NW, image=self.frames[self.current_frame])
        self.update_animation_frames()
        self.waiting_animation()

    def waiting_animation(self):
        self.current_frame = (self.current_frame + 1) % len(self.waiting_animation_frames)
        self.canvas.config(width=self.frames_width[0], height=self.y)
        self.canvas.itemconfig(self.canvas.find_all()[0], image=self.waiting_animation_frames[self.current_frame])
        self.canvas.after(self.ANIMATION_SPEED, self.waiting_animation)
        