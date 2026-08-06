class MonitorInfo:
    def __init__(
        self,
        name: str,
        left: int,
        top: int,
        width: int,
        height: int,
        dpi: int = 96
    ):
        self.name = name

        self.left = left
        self.top = top

        self.width = width
        self.height = height

        self.dpi = dpi

    @property
    def right(self):
        return self.left + self.width

    @property
    def bottom(self):
        return self.top + self.height