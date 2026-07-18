import time
from core.events.event_bus import EventBus
from core.events import event_types

class Engine:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.running = False
        self.fps = 60 # TODO: Make this configurable
        self.frame_time = 1.0 / self.fps

    def start(self):
        self.running = True
        
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