import numpy as np

from ..vertices import Vertices


class Sphere:
    """A parametric sphere"""

    def __init__(self, n: int):
        self._n = n
        self._vertices = self._compute_vertices(n)

    @staticmethod
    def _compute_vertices(n: int) -> Vertices:
        us = np.arange(0, 2 * np.pi, 2 * np.pi / n)
        vs = np.arange(0, 2 * np.pi, 2 * np.pi / n)
        data = np.array(
            [
                np.array([np.cos(u) * np.cos(v), np.cos(u) * np.sin(v), np.sin(u)])
                for u in us
                for v in vs
            ]
        )
        return Vertices(data)

    @property
    def vertices(self) -> Vertices:
        return self._vertices
