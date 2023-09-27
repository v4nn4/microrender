import math

import numpy as np


class Point:
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self) -> float:
        return self._z

    def snorm(self):
        x = self._x
        y = self._y
        z = self._z
        return x * x + y * y + z * z

    def to_array(self) -> np.ndarray:
        return np.array([self._x, self._y, self._z], dtype=float)

    def normalize(self) -> "Point":
        norm = math.sqrt(self.snorm())
        return Point(self._x / norm, self._y / norm, self._z / norm)

    def __repr__(self) -> str:
        return f"x={self._x}, y={self._y}, z={self._z}"
