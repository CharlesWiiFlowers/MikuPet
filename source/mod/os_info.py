import win32gui

def get_active_window_bottom():
    """
    Get the bottom position of the currently active window.
    Returns:
        int: The bottom position of the active window.
    """
    try:
        hwnd = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hwnd)
        #print(rect)  # Debugging: print the rectangle coordinates
        return rect[3]  # Return the bottom coordinate of the window rectangle
    except Exception as e:
        print(f"Error getting active window bottom: {e}")
        return 0