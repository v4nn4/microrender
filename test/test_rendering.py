import numpy as np
import pytest

from microrender.point import Point
from microrender.vertices import Vertices
from microrender.window import Window


@pytest.mark.parametrize("use_quaternions", [True, False])
def test_rendering(use_quaternions: bool):
    width, height = 50, 50
    window = Window(width, height)
    vertices = Vertices(
        [
            Point(0.25, 0.0, 0.0),
            Point(-0.25, 0.0, 0.0),
            Point(0.0, 0.25, 0.0),
            Point(0.0, -0.25, 0.0),
        ]
    )
    array = window.render(vertices)
    assert array.shape == (width, height, 3)
    rotation_axis, angle = Point(0, 0, 1), 0.1
    vertices.rotate(rotation_axis, angle, use_quaternions)
    rotated_array = window.render(vertices)
    assert array.shape == (width, height, 3)
    assert np.not_equal(array, rotated_array).any()


@pytest.mark.parametrize("use_quaternions", [True, False])
def test_rotation_undo(use_quaternions: bool):
    rotation_axis, angle = Point(0, 0, 1), 0.1
    vertices = Vertices(
        [
            Point(0.25, 0.0, 0.0),
            Point(-0.25, 0.0, 0.0),
            Point(0.0, 0.25, 0.0),
            Point(0.0, -0.25, 0.0),
        ]
    )
    vertices.rotate(rotation_axis, angle, use_quaternions)
    vertices.rotate(rotation_axis, -angle, use_quaternions)
    assert vertices.data[0][0] == 0.25
    assert vertices.data[1][0] == -0.25
    assert vertices.data[2][1] == 0.25
    assert vertices.data[3][1] == -0.25


def test_quaternion_rotation():
    rotation_axis, angle = Point(0, 0, 1), 0.1
    points = [
        Point(0.25, 0.0, 0.0),
        Point(-0.25, 0.0, 0.0),
        Point(0.0, 0.25, 0.0),
        Point(0.0, -0.25, 0.0),
    ]
    vertices = Vertices(points)
    vertices.rotate(rotation_axis, angle, use_quaternions=True)
    vertices_copy = Vertices(points.copy())
    vertices_copy.rotate(rotation_axis, angle, use_quaternions=False)
    assert (vertices.data == vertices_copy.data).all()
