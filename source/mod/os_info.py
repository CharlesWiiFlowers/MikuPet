import win32gui

def get_active_window(side:int = 0) -> int:
    """
    Get the coordinates of the active window.
    :param side: 0 for top, 1 for left, 2 for right, 3 for bottom
    :return: The coordinate of the specified side of the active window.
    """
    try:
        hwnd = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(hwnd)
        #print(rect)  # Debugging: print the rectangle coordinates
        
        left, top, right, bottom = rect

        match side:
            case 0:  # Return the top coordinate of the window rectangle
                return top
            case 1:  # Return the left coordinate of the window rectangle
                return left
            case 2:  # Return the right coordinate of the window rectangle
                return right
            case _ :  # Default case, return the bottom coordinate of the window rectangle
                return bottom

    except Exception as e:
        print(f"Error getting active window bottom: {e}")
        return 0