import tkinter
import threading
import warnings
from mod.sprites import Animation
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

class AppBroadcast(AppUI):
    def __init__(self):
        super().__init__()
        self.running = True
        threading.Thread(target=self.listen_to_console, daemon=True).start()
        
        # Create the main window
        self.mainloop()
        
    def listen_to_console(self):
        while self.running:
            # This thread can be used to listen to console input or other events
            try:
                command = input()
                if command.lower() == 'miku bye' or command.lower() == 'bye':
                    self.running = False
                    self.broadcast("Goodbye~!! 💕👋.")
                    self.stop()
                else:
                    self.broadcast("I do not understand you~ 🥺")
            except EOFError as e:
                warnings.warn(f"Error: {e}")
                break
    
    def broadcast(self, text:str):
        print(f"Miku: {text}")

    def run(self):
        # This thread can be used for broadcasting messages or handling background tasks
        pass

if __name__ == "__main__":
    # Start the program
    AppBroadcast().listen_to_console()
    #AppUI().mainloop()