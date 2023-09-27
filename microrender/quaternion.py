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

    def _to_point(self) -> Point:
        return Point(self._b, self._c, self._d)

    def __mul__(self, q):
        a = self.a * q.a - self.b * q.b - self.c * q.c - self.d * q.d
        b = self.a * q.b + self.b * q.a + self.c * q.d - self.d * q.c
        c = self.a * q.c - self.b * q.d + self.c * q.a + self.d * q.b
        d = self.a * q.d + self.b * q.c - self.c * q.b + self.d * q.a
        return Quaternion(a, b, c, d)

    def squared_norm(self) -> float:
        a = self._a
        b = self._b
        c = self._c
        d = self._d
        return a * a + b * b + c * c + d * d

    @staticmethod
    def conjugate(vertex: Point, quaternion: "Quaternion") -> "Quaternion":
        reciprocal = quaternion.reciprocal()
        vertex_as_quaternion = Quaternion(0, vertex.x, vertex.y, vertex.z)
        return quaternion * vertex_as_quaternion * reciprocal

    def reciprocal(self) -> "Quaternion":
        one_over_sn = 1 / self.squared_norm()
        a = self._a
        b = self._b
        c = self._c
        d = self._d
        return Quaternion(
            a * one_over_sn, -b * one_over_sn, -c * one_over_sn, -d * one_over_sn
        )

    @staticmethod
    def versor(axis: Point, angle: float) -> "Quaternion":
        mid_angle = angle * 0.5
        sin = math.sin(mid_angle)
        cos = math.cos(mid_angle)
        return Quaternion(cos, sin * axis.x, sin * axis.y, sin * axis.z)

    @staticmethod
    def rotate(vertex: Point, versor: "Quaternion") -> Point:
        return Quaternion.conjugate(vertex, versor)._to_point()

    def __repr__(self) -> str:
        return f"a={self.a}, b={self.b}, c={self.c}, d={self.d}"
