from pathlib import Path
import tkinter as tk

from core.file_system import FileSystem
from objects.leek import Leek


class LeekLoader:

    def __init__(self) -> None:
        self.project_root = FileSystem.root()
        self.project_root.mkdir(exist_ok=True)

    def load(self) -> Leek:

        leek = Leek()

        leek.image = tk.PhotoImage(
            file=self.project_root / "assets" / "objects" / "leek.png"
        )

        leek.width = leek.image.width()
        leek.height = leek.image.height()

        return leek