from objects.object import Object

class Leek(Object):

    def __init__(self) -> None:
        super().__init__()

        self.miku_reaction = "walk_to"

        self.gravity = 0.5
        self.gravity_velocity = 0

    def update(self) -> None:

        if not self.is_falling:
            return

        self.gravity_velocity += self.gravity

        self.position["y"] += self.gravity_velocity