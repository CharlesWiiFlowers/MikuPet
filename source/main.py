import os
from mod.settings import load_settings, TEMPLATE

CHARACTER_FOLDER:list[str] = [item for item in os.listdir("./assets/") if "." not in item]

print(CHARACTER_FOLDER)

class Main():
    def __init__(self) -> None:
        self.settings = load_settings() if load_settings() != None else TEMPLATE

    def validations(self) -> None:
        if self.settings["selected_character"] in CHARACTER_FOLDER: # type: ignore
            # :p

if __name__ == "__main__":
    Main()