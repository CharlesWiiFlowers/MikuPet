import tkinter
import math
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
        #print(f"Clicked at {event.x}, {event.y}")
        pass

    def handle_motion(self, event:tkinter.Event):
        if self.press:
            # If the mouse button is pressed, we can handle dragging or other actions
            self.reference.geometry(f"+{event.x_root}+{event.y_root}")
            #print(f"Mouse dragged to {event.x}, {event.y}")
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
        self.GRAVITY:int = 1 # Gravity constant, can be adjusted for different effects
        self.MILLISECONDS:int = milliseconds # Delay in milliseconds for gravity checks
        self.reference.bind("<FocusIn>", self.handle_focus_in)  # Stop gravity when the canvas gets focus, i know this is counterintuitive
        self.reference.bind("<FocusOut>", self.handle_focus_out)  # Start gravity when the canvas loses focus
        self.has_focus = False

    def handle_focus_in(self, event:tkinter.Event):
        """Handle focus in event to stop gravity checks."""
        self.has_focus = True

    def handle_focus_out(self, event:tkinter.Event):
        """Handle focus out event to start gravity checks."""
        self.has_focus = False

    def gravity(self, enabled:bool = True):
        if not enabled:
            return

        if not self.has_focus:
            # If Miku is not focused, we can apply gravity

            y = self.reference.winfo_y()
            active_window_bottom = mod.os_info.get_active_window(3) - self.reference.winfo_height() - 10  # Get the bottom coordinate of the active window - 10px margin - the height of Miku
            gravity_velocity = math.ceil(math.sqrt(2 * self.GRAVITY * (y + 0.1)))  # Calculate the gravity velocity based on the GRAVITY value
            print(gravity_velocity)

            if ((y < (active_window_bottom)) and ((y + gravity_velocity) > (active_window_bottom))):
                print("o")
                gravity_velocity = 1

            # Check if Miku is upper than the active window bottom
            if(y < (active_window_bottom)): # 10px margin
                self.isFlying = True
                # Move Miku down by GRAVITY_VELOCITY pixels
                # This is to simulate gravity, Miku will fall down
                self.reference.geometry(f"+{self.reference.winfo_x()}+{y + gravity_velocity}")
            # Check if Miku is lower than the active window bottom
            elif(y > (active_window_bottom)):
                self.isFlying = True
                self.reference.geometry(f"+{self.reference.winfo_x()}+{y - gravity_velocity}") # 10px margin                
            else:
                # If Miku is at the bottom of the active window, stop flying
                self.isFlying = False

        # Schedule the next gravity check
        self.reference.after(self.MILLISECONDS, self.gravity)