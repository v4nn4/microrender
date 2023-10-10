import math

import numpy as np

from .rotatable import Rotatable


class Matrix(Rotatable):
    def __init__(self, matrix: np.ndarray):
        self._matrix = matrix

    @staticmethod
    def rotatable(axis: np.ndarray, theta: float) -> Rotatable:
        """
        Return the rotation matrix associated with counterclockwise rotation about
        the given axis by theta radians
        """
        axis = np.asarray(axis)
        axis = axis / math.sqrt(np.dot(axis, axis))
        a = math.cos(theta / 2.0)
        b, c, d = -axis * math.sin(theta / 2.0)
        aa, bb, cc, dd = a * a, b * b, c * c, d * d
        bc, ad, ac, ab, bd, cd = b * c, a * d, a * c, a * b, b * d, c * d
        return Matrix(
            np.array(
                [
                    [aa + bb - cc - dd, 2 * (bc + ad), 2 * (bd - ac)],
                    [2 * (bc - ad), aa + cc - bb - dd, 2 * (cd + ab)],
                    [2 * (bd + ac), 2 * (cd - ab), aa + dd - bb - cc],
                ]
            )
        )

    def rotate(self, point: np.ndarray) -> np.ndarray:
        return np.dot(self._matrix, point)
