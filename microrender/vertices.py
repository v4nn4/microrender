import typing

import numpy as np
import open3d as o3d

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
        for i in range(len(self._data)):
            x, y, z = self._data[i, :]
            rotated_vertex = Quaternion.rotate(Point(x, y, z), versor).to_array()
            self._data[i, :] = rotated_vertex

    def distance(self, point: Point) -> float:
        data = self._data
        array = point.to_array()
        return np.min(np.sqrt(((data - array) * (data - array)).sum(axis=1)))

    @staticmethod
    def from_ply(
        filename: str,
        scale: float = 1.0,
        shift: Point = Point(0, 0, 0),
        voxel_size: float = 0.01,
    ) -> "Vertices":
        pcd = o3d.io.read_point_cloud(filename)
        low_pcd = pcd.voxel_down_sample(voxel_size)  # downsample
        xyzs = np.asarray(low_pcd.points) * scale
        dx, dy, dz = shift.x, shift.y, shift.z
        return Vertices([Point(v[0] + dx, v[1] + dy, v[2] + dz) for v in xyzs])

    def __repr__(self) -> str:
        return f"{self._data}"
