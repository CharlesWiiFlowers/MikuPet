from dataclasses import dataclass
from datetime import datetime
from typing import Any

@dataclass(frozen=True, slots=True, kw_only=True)
class Event():
    event_type: str
    data: Any
    timestamp: datetime
    source: str | None