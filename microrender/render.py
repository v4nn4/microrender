from typing import Callable

import numpy as np
from PIL import Image

from .point import Point
from .vertices import Vertices


def gaussian_kernel(beta: float) -> Callable[[float], float]:
    return lambda x: np.exp(-beta * x * x)


class Window:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def _get_embedded_coordinates(self, i: int, j: int) -> Point:
        x = (i - self._width / 2) / self._width
        y = (j - self._height / 2) / self._height
        return Point(x, y, 0)

    def render(self, vertices: Vertices, beta=10000):
        width = self._width
        height = self._height
        window = np.zeros(shape=(width, height, 3), dtype=np.uint8)
        kernel = gaussian_kernel(beta)
        for i in range(width):
            for j in range(height):
                vertex = self._get_embedded_coordinates(i, j)
                distance = vertices.distance(vertex)
                color = np.maximum(0, np.minimum(255, kernel(distance) * 255))
                window[i, j, :] = [color] * 3
        return Image.fromarray(window)
