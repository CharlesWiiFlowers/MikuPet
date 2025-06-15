import tkinter

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
            print(f"Mouse dragged to {event.x}, {event.y}")
        else:
            # Handle mouse movement without pressing
            print(f"Mouse moved to {event.x}, {event.y}")

    def handle_press(self, event:tkinter.Event):
        self.press = True
        print(f"Mouse button pressed at {event.x}, {event.y}")

    def handle_release(self, event:tkinter.Event):
        self.press = False
        print(f"Mouse button released at {event.x}, {event.y}")
