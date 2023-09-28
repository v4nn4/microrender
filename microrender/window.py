from typing import Tuple

import numpy as np

from .vertices import Vertices


class Window:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def world_to_view(self, x: float, y: float) -> Tuple[int, int]:
        return (
            np.floor(self._width * x + self._width / 2).astype(int),
            np.floor(self._height * y + self._height / 2).astype(int),
        )

    def render(self, vertices: Vertices) -> np.ndarray:
        width = self._width
        height = self._height
        window = np.zeros(shape=(width, height, 3), dtype=np.uint8) * 255
        for vertex in vertices.data:
            i, j = self.world_to_view(vertex[0], vertex[1])
            i, j = np.clip(i, 0, width - 1), np.clip(j, 0, height - 1)
            window[i, j, :] = [255] * 3
        inverted_window = 255 - window  # black over white
        return inverted_window
