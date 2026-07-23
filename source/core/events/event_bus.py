"""
Event system.

Allows different modules to communicate
without depending on one another.

File used as a reference: https://github.com/CharlesWiiFlowers/JARVIS/blob/05b80196d90352a45004120988f4fb678bddbb84/core/events/event_bus.py
"""

from datetime import datetime
from typing import Any, Callable

from core.events.events import Event
from core.events import event_types

class EventBus:

    def __init__(self):
        self.listeners: dict[str, list[Callable[[Event]]]] = {}
        self.global_listeners: list[Callable[[Event]]] = []

    def on(self, event_name:str, callback: Callable[[Event]]):
        """Subscribe to an event.

        Args:
            event_name (str): Define a name to hear it..
            callback (function): The callback will be executed whenever the specified event is emitted.
        """

        if event_name not in self.listeners:
            self.listeners[event_name] = []

            # Notify: New event created
            self.emit(
                event_types.EVENT_NEW,
                source=self)

        self.listeners[event_name].append(callback)

    def on_all(self, callback: Callable[[Event]]):
        """Subscribe to every event.

        Args:
            callback (function): The function to call whenever the events are on.
        """

        self.global_listeners.append(callback)
        
    def emit(self, event_name:str, data:Any = None, source:object | None=None):
        """Emit an event.

        Args:
            event_name (str): Name of the event to emit.
            data (Any, optional): Any type of data to transmit. Defaults to None.
            source (object | None, optional): Whose emit the event. Defaults to None.
        """

        if event_name not in self.listeners: return

        event = Event(
            event_type=event_name,
            data=data,
            timestamp=datetime.now(),
            source=source
        )

        for callback in self.listeners[event_name]:
            callback(event)

        for callback in self.global_listeners:
            callback(event)

        if event_name != event_types.EVENT_EMIT: self.emit(event_name=event_types.EVENT_EMIT, source=self)