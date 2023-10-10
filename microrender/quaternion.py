import math

import numpy as np

from .point import Point


class Quaternion:
    def __init__(self, a: float, b: float, c: float, d: float):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
        self.initialize_rotation_matrix()

    @property
    def a(self) -> float:
        return self._a

    @property
    def b(self) -> float:
        return self._b

    @property
    def c(self) -> float:
        return self._c

    @property
    def d(self) -> float:
        return self._d

    def initialize_rotation_matrix(self):
        a = self.a
        b = self.b
        c = self.c
        d = self.d
        t2 = a * b
        t3 = a * c
        t4 = a * d
        t5 = -b * b
        t6 = b * c
        t7 = b * d
        t8 = -c * c
        t9 = c * d
        t10 = -d * d
        self._R = np.array(
            [
                [1 + 2 * (t8 + t10), 2 * (t6 - t4), 2 * (t3 + t7)],
                [2 * (t4 + t6), 1 + 2 * (t5 + t10), 2 * (t9 - t2)],
                [2 * (t7 - t3), 2 * (t2 + t9), 1 + 2 * (t5 + t8)],
            ]
        )

    @staticmethod
    def versor(axis: Point, theta: float) -> "Quaternion":
        mid_angle = theta * 0.5
        sin = math.sin(mid_angle)
        cos = math.cos(mid_angle)
        return Quaternion(cos, sin * axis.x, sin * axis.y, sin * axis.z)

    def rotate(self, point: np.ndarray) -> np.ndarray:
        return np.dot(self._R, point)

    def __repr__(self) -> str:
        return f"a={self.a}, b={self.b}, c={self.c}, d={self.d}"
