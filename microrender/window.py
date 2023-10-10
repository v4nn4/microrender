import numpy as np

from .vertices import Vertices


class Window:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def world_to_positions(self, vertices: Vertices) -> np.ndarray:
        """Converts the (x, y) world coordinates to (i, j) pixel positions

        Formula:
          i, j = w * x + 0.5 * w, h * y + 0.5 * h
        """
        projection = vertices.data[:, :2]  # remove z-axis
        positions = np.floor(
            projection * [self._width, self._height]
            + [0.5 * self._width, 0.5 * self._height]
        ).astype(int)
        return positions

    def render(self, vertices: Vertices) -> np.ndarray:
        """Initialize view to 0s, only paint pixels corresponding to vertices"""
        width = self._width
        height = self._height
        window = np.zeros(shape=(width, height, 3), dtype=np.uint8)
        positions = self.world_to_positions(vertices)  # (W, H)
        positions = np.stack(
            (
                np.clip(positions[:, 0], 0, width),
                np.clip(positions[:, 1], 0, height),
            ),
            axis=-1,
        )
        color = np.array([255, 255, 255])  # black
        window[positions[:, 0], positions[:, 1], :] = color
        inverted_window = 255 - window  # black over white
        return inverted_window
