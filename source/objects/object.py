class Object:

    def __init__(self) -> None:

        self.position: dict[str, float] = {
            "x": 0,
            "y": 0
        }

        self.width = 0
        self.height = 0

        self.is_grabbable = True
        self.is_falling = True

    def update(self) -> None:
        pass