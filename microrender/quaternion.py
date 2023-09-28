import math

from .point import Point


class Quaternion:
    def __init__(self, a: float, b: float, c: float, d: float):
        self._a = a
        self._b = b
        self._c = c
        self._d = d

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

    @staticmethod
    def versor(axis: Point, theta: float) -> "Quaternion":
        mid_angle = theta * 0.5
        sin = math.sin(mid_angle)
        cos = math.cos(mid_angle)
        return Quaternion(cos, sin * axis.x, sin * axis.y, sin * axis.z)

    @staticmethod
    def rotate(point: Point, versor: "Quaternion") -> Point:
        x = point.x
        y = point.y
        z = point.z
        a = versor.a
        b = versor.b
        c = versor.c
        d = versor.d
        t2 = a * b
        t3 = a * c
        t4 = a * d
        t5 = -b * b
        t6 = b * c
        t7 = b * d
        t8 = -c * c
        t9 = c * d
        t10 = -d * d
        x_ = 2 * ((t8 + t10) * x + (t6 - t4) * y + (t3 + t7) * z) + x
        y_ = 2 * ((t4 + t6) * x + (t5 + t10) * y + (t9 - t2) * z) + y
        z_ = 2 * ((t7 - t3) * x + (t2 + t9) * y + (t5 + t8) * z) + z
        return Point(x_, y_, z_)

    def __repr__(self) -> str:
        return f"a={self.a}, b={self.b}, c={self.c}, d={self.d}"
