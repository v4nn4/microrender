import numpy as np
import open3d as o3d

from .rotatable import Rotatable


class Vertices:
    """
    Set of points represented by an array of shape (nb_points, 3)
    """

    def __init__(self, data: np.ndarray):
        assert len(data.shape) == 2
        N, D = data.shape
        assert D == 3  # 3d
        assert N > 1, "Need at least one point"
        self._data = data

    @property
    def data(self) -> np.ndarray:
        return self._data

    def rotate(self, rotatable: Rotatable):
        self._data = rotatable.rotate(self._data.T).T

    def distance(self, point: np.ndarray) -> float:
        data = self._data
        return np.min(np.sqrt(((data - point) * (data - point)).sum(axis=1)))

    @staticmethod
    def from_ply(
        filename: str,
        scale: float = 1.0,
        shift: np.ndarray = np.zeros(3),
        voxel_size: float = 0.01,
    ) -> "Vertices":
        pcd = o3d.io.read_point_cloud(filename)
        low_pcd = pcd.voxel_down_sample(voxel_size)  # downsample
        data = np.asarray(low_pcd.points) * scale + shift
        return Vertices(data)

    def __len__(self) -> int:
        return self._data.shape[0]

    def __repr__(self) -> str:
        return f"{self._data}"
