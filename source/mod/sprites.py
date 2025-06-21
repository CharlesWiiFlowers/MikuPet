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
        self.walking_animation_frames = []
        self.jumping_animation_frames = []
        self.sneezing_animation_frames = []
        self.coloring_animation_frames = []

        self.current_frame = 0
        self.BACKGROUND_COLOR = background_color
        self.canvas = tkinter.Canvas(width=initial_x, height=self.y, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

        self.sprite_sheet()  # Load the sprite sheet and initialize frames
        self.update_animation_frames()  # Update the animation frames based on the sprite sheet

    def update_animation_frames(self):
        """Update the animation frames based on the sprite sheet."""
        
        self.waiting_animation_frames = self.frames[:19]  # Use the first 20 frames for the waiting animation
        self.walking_animation_frames = self.frames[20:26]  # Use the next 8 frames for the walking animation
        self.jumping_animation_frames = self.frames[29:37]  # Use the next 9 frames for the jumping animation
        self.sneezing_animation_frames = self.frames[38:46]  # Use the next 8 frames for the sneezing animation
        self.coloring_animation_frames = self.frames[47:49]  # Use the next 3 frames for the coloring animation
        # Frame 50 won't be used in any animation
        self.dragging_animation_frames = self.frames[51:53]  # Use the next 2 frames for the dragging animation
        self.sleeping_animation_frames = self.frames[54:54]  # Use the next 1 frames for the sleeping animation
        self.dancing_animation_frames = self.frames[55:67]  # Use the next 12 frames for the dancing animation

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
        
class Animation(Sprite):
    def __init__(self, image_path:list[str], sprite_number_of, initial_x = 59, initial_y = 100, animation_speed:int = 100, background_color:str = "#96C8FA"):
        super().__init__(image_path, sprite_number_of, initial_x, initial_y, animation_speed, background_color)
        self.animation_list:int = 0
        # 0: Waiting animation; 1: Walking animation; 2: Jumping animation; 3: Sneezing animation; 4: Coloring animation; 5: Dragging animation; 6: Sleeping animation; 7: Dancing animation

    def animation(self):
        """
        Start the animation.
        :change self.animation_list
        :0: Waiting animation; 1: Walking animation; 2: Jumping animation; 3: Sneezing animation; 4: Coloring animation; 5: Dragging animation; 6: Sleeping animation; 7: Dancing animation
        :return: None
        """
        #self.animation_list = animation

        #if animation == 0:
            # Start the waiting animation
         #   self.update_animation_frames()
         #   self.waiting_animation()
        #self.waiting_animation_frames.clear()

        match self.animation_list:
            case 0:
                self.current_frame = (self.current_frame + 1) % len(self.waiting_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.waiting_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 1:
                self.current_frame = (self.current_frame + 1) % len(self.walking_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.walking_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 2:
                self.current_frame = (self.current_frame + 1) % len(self.jumping_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.jumping_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 3:
                self.current_frame = (self.current_frame + 1) % len(self.sneezing_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.sneezing_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 4:
                self.current_frame = (self.current_frame + 1) % len(self.coloring_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.coloring_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 5:
                self.current_frame = (self.current_frame + 1) % len(self.dragging_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.dragging_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 6:
                self.current_frame = (self.current_frame + 1) % len(self.sleeping_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.sleeping_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case 7:
                self.current_frame = (self.current_frame + 1) % len(self.dancing_animation_frames)
                self.canvas.config(width=self.frames_width[0], height=self.y)
                self.canvas.itemconfig(self.canvas.find_all()[0], image=self.dancing_animation_frames[self.current_frame])
                self.canvas.after(self.ANIMATION_SPEED, self.animation)
            case _:
                warnings.warn(f"Animation {self.animation_list} not implemented. Reseting to default animation.", UserWarning)
                self.animation_list = 0  # Reset to default waiting animation if not implemented