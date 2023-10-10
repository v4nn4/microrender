from typing import Protocol

import numpy as np


class Rotatable(Protocol):
    def rotate(self, point: np.ndarray) -> np.ndarray:
        ...
