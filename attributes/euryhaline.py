from attributes import Aquatic


class Euryhaline(Aquatic):
    def __init__(self):
        super().__init__()
        self.is_euryhaline = True
        self.cell_type = ["hypertonic", "hypotonic"]
