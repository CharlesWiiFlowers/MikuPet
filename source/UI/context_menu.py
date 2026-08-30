"""
MikuPet context menu.
"""

import tkinter as tk

from core.events.event_bus import EventBus
from core.character import Character
from core.events.event_types import (
    EVENT_CONTEXT_MENU_REQUESTED,
    EVENT_ACTION_REQUESTED_KILL
)


class ContextMenu:

    def __init__(self, bus: EventBus, character: Character):

        self.bus = bus

        self.character = character

        self.window = None

        self.bus.on(
            EVENT_CONTEXT_MENU_REQUESTED,
            self._on_context_menu_requested
        )

    def _on_context_menu_requested(self, event):
        self.character.set_focus()

        x = event.data["x"] + 50
        y = event.data["y"] - 100

        self._show(x, y)

    def _show(self, x: int, y: int):

        if self.window is not None:
            self._close()

        self.window = tk.Toplevel()

        self.window.overrideredirect(True)
        self.window.attributes("-topmost", True)

        # Miku colors
        background = "#1B263B"
        panel = "#2E3A59"
        accent = "#39C5BB"
        accent_hover = "#5DE2D6"
        text = "#FFFFFF"

        self.window.configure(
            bg=accent
        )

        container = tk.Frame(
            self.window,
            bg=panel,
            bd=0
        )
        container.pack(
            padx=2,
            pady=2
        )

        title = tk.Label(
            container,
            text="Do an action",
            font=("Segoe UI", 10, "bold"),
            fg=accent,
            bg=panel,
            padx=16,
            pady=10
        )
        title.pack(
            fill="x"
        )

        kill_button = tk.Button(
            container,
            text="Kill",
            font=("Segoe UI", 9),
            fg=text,
            bg=panel,
            activeforeground=text,
            activebackground=accent,
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=18,
            pady=7,
            command=self._kill
        )
        kill_button.pack(
            fill="x",
            padx=6,
            pady=(0, 6)
        )

        self.window.update_idletasks()

        self.window.geometry(
            f"+{x}+{y}"
        )

        self.window.bind(
            "<FocusOut>",
            lambda event: self._close()
        )

        self.window.focus_force()

    def _kill(self):

        self.bus.emit(
            EVENT_ACTION_REQUESTED_KILL,
            source=self
        )

        self._close()

    def _close(self):

        if self.window is None:
            return

        try:
            self.window.destroy()
        except tk.TclError:
            pass

        self.window = None

        self.character.set_focus(False)