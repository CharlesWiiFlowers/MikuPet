import json
import warnings
from .typething import Setting

TEMPLATE:Setting = {
    "selected_character": "miku"
}

def load_settings(path="settings.json") -> Setting | None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            settings: Setting = json.load(file)

        return settings

    except:
        warnings.warn(f"[ERROR] Settings not found. Please generate a setting file.", UserWarning)