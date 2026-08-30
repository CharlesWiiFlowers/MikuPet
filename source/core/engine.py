import time
from core.events.event_bus import EventBus
from core.events import event_types

class Engine:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.config = {}
        self.running = False
        self.fps = 60
        self.frame_time = 1.0 / self.fps

        self.bus.on(
            event_types.EVENT_CONFIG_LOADED,
            callback=self._load_config
        )

        self.bus.on(
            event_types.EVENT_CONFIG_UPDATE,
            self._update_config
        )

        self.bus.on(
            event_name=event_types.EVENT_ACTION_REQUESTED_KILL,
            callback=self._on_kill
        )

    def start(self):
        self.running = True

        self.fps = self.config["fps"]
        
        while self.running:
            start_time = time.time()

            # 1. LEER SENSORES: Actualizamos información del sistema, ventanas, inputs.
            self.bus.emit(event_types.ENGINE_PRE_UPDATE)

            # 2. PROCESAR LÓGICA: Gravedad, movimiento, inteligencia artificial.
            self.bus.emit(event_types.ENGINE_UPDATE)

            # 3. ACTUADORES: Dibujar a Miku en la pantalla.
            self.bus.emit(event_types.ENGINE_RENDER)

            # Control de los FPS (para que no consuma 100% del CPU)
            elapsed = time.time() - start_time
            sleep_time = self.frame_time - elapsed
            if sleep_time > 0:
                time.sleep(sleep_time)

    def _load_config(self, event):
        self.config = event.source

    def _update_config(self, event):
        self._load_config(event=event)

    def _on_kill(self, event):
        self.running = False