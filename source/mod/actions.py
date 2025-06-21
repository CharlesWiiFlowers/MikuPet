import tkinter
import mod.os_info

class Actions(tkinter.Frame):
    def __init__(self, Canvas:tkinter.Canvas, reference:tkinter.Tk):
        self.canvas = Canvas
        self.press:bool = False
        self.reference = reference
        self.canvas.bind("<Button-1>", self.handle_click)
        self.canvas.bind("<Motion>", self.handle_motion)
        self.canvas.bind("<ButtonPress-1>", self.handle_press)
        self.canvas.bind("<ButtonRelease-1>", self.handle_release)

    def handle_click(self, event:tkinter.Event):
        print(f"Clicked at {event.x}, {event.y}")

    def handle_motion(self, event:tkinter.Event):
        if self.press:
            # If the mouse button is pressed, we can handle dragging or other actions
            self.reference.geometry(f"+{event.x_root}+{event.y_root}")
            #print(f"Mouse dragged to {event.x}, {event.y}")
            print(f"{self.reference.winfo_y() + self.reference.winfo_height()}")
        else:
            # Handle mouse movement without pressing
            #print(f"Mouse moved to {event.x}, {event.y}")
            pass

    def handle_press(self, event:tkinter.Event):
        self.press = True
        #print(f"Mouse button pressed at {event.x}, {event.y}")

    def handle_release(self, event:tkinter.Event):
        self.press = False
        #print(f"Mouse button released at {event.x}, {event.y}")

class AutoActions(tkinter.Frame):
    def __init__(self, Canvas:tkinter.Canvas, reference:tkinter.Tk, milliseconds:int = 16):
        self.canvas = Canvas
        self.reference = reference
        self.isFlying:bool = False
        self.GRAVITY_VELOCITY:int = 1 # TODO: Make this an exponential value
        # Default milliseconds for gravity check, can't be ajusted for now
        # Bug: If this is not set to 1, the gravity will not work properly
        self.MILLISECONDS:int = milliseconds

    def gravity(self, enabled:bool = True):
        if not enabled:
            return

        y = self.reference.winfo_y()

        if(y < (mod.os_info.get_active_window_bottom() - self.reference.winfo_height() - 10)): # 10px margin
            self.isFlying = True
            self.reference.geometry(f"+{self.reference.winfo_x()}+{y + self.GRAVITY_VELOCITY}")
            print(f" {y + self.GRAVITY_VELOCITY} < {mod.os_info.get_active_window_bottom() - self.reference.winfo_height()}")
        elif(y > (mod.os_info.get_active_window_bottom() - self.reference.winfo_height() - 10)):
            self.isFlying = True
            self.reference.geometry(f"+{self.reference.winfo_x()}+{y - self.GRAVITY_VELOCITY}")
            print(f" {y + self.GRAVITY_VELOCITY} < {mod.os_info.get_active_window_bottom() - self.reference.winfo_height()}")
        else:
            self.isFlying = False

        self.reference.after(self.MILLISECONDS, self.gravity)