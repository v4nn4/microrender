import typing

import numpy as np

from .point import Point
from .quaternion import Quaternion


class Vertices:
    """
    Set of points represented by an array of shape (nb_points, 3)
    """

    def __init__(self, vertices: typing.List[Point]):
        assert isinstance(vertices, list)
        for point in vertices:
            assert isinstance(point, Point)
        self._data = np.zeros(shape=(len(vertices), 3), dtype=float)
        for i, point in enumerate(vertices):
            self._data[i, :] = point.to_array()

    @property
    def data(self) -> np.ndarray:
        return self._data

    def rotate(self, axis: Point, angle: float):
        versor = Quaternion.versor(axis, angle)
        print(versor)
        for i in range(len(self._data)):
            x, y, z = self._data[i, :]
            rotated_vertex = Quaternion.rotate(Point(x, y, z), versor).to_array()
            self._data[i, :] = rotated_vertex

    def distance(self, point: Point) -> float:
        data = self._data
        array = point.to_array()
        return np.min(np.sqrt(((data - array) * (data - array)).sum(axis=1)))

    def __repr__(self) -> str:
        return f"{self._data}"
