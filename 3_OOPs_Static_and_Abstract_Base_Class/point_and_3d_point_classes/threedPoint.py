class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def display(self):
        print(f"[{self._x}, {self._y}]")


class ThreedPoint(Point):
    def __init__(self, x, y, z):
        # """Todo for the learner"""
        super().__init__(x, y)
        self._z = z

    def display(self):
        # """Todo for the learner"""
        print(f"[{self._x}, {self._y}, {self._z}]")