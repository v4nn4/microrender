import numpy as np

from .vertices import Vertices


class Window:
    """Renders pixels to screen"""

    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    def world_to_view(self, vertices: Vertices) -> np.ndarray:
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

        # Initialize pixels to white
        window = np.zeros(shape=(width, height, 3), dtype=np.uint8)

        # Convert world coordinates to view coordinates (window indices)
        pixels = self.world_to_view(vertices)

        # Keep only pixels visible in the window
        pixels = pixels[
            np.logical_and(
                np.logical_and(pixels[:, 0] >= 0, pixels[:, 0] < width),
                np.logical_and(
                    pixels[:, 1] >= 0,
                    pixels[:, 1] < height,
                ),
            )
        ]

        # Paint window in white at pixels' location
        color = np.array([255, 255, 255])  # white
        window[pixels[:, 0], pixels[:, 1], :] = color

        # Invert colors
        inverted_window = 255 - window

        return inverted_window
