import numpy as np
import pytest

from microrender import Vertices, Quaternion, Matrix, Window


@pytest.mark.parametrize("use_quaternions", [True, False])
def test_rendering(use_quaternions: bool):
    width, height = 50, 50
    window = Window(width, height)
    vertices = Vertices(
        np.array(
            [[0.25, 0.0, 0.0], [-0.25, 0.0, 0.0], [0.0, 0.25, 0.0], [0.0, -0.25, 0.0]]
        )
    )
    array = window.render(vertices)
    assert array.shape == (width, height, 3)
    rotation_axis, angle = np.array([0, 0, 1]), 0.1
    rotatable = (
        Quaternion.rotatable(rotation_axis, angle)
        if use_quaternions
        else Matrix.rotatable(rotation_axis, angle)
    )
    vertices.rotate(rotatable)
    rotated_array = window.render(vertices)
    assert array.shape == (width, height, 3)
    assert np.not_equal(array, rotated_array).any()


@pytest.mark.parametrize("use_quaternions", [True, False])
def test_rotation_undo(use_quaternions: bool):
    rotation_axis, angle = np.array([0, 0, 1]), 0.1
    vertices = Vertices(
        np.array(
            [[0.25, 0.0, 0.0], [-0.25, 0.0, 0.0], [0.0, 0.25, 0.0], [0.0, -0.25, 0.0]]
        )
    )
    rotatable = (
        Quaternion.rotatable(rotation_axis, angle)
        if use_quaternions
        else Matrix.rotatable(rotation_axis, angle)
    )
    vertices.rotate(rotatable)
    rotatable = (
        Quaternion.rotatable(rotation_axis, -angle)
        if use_quaternions
        else Matrix.rotatable(rotation_axis, -angle)
    )
    vertices.rotate(rotatable)
    assert vertices.data[0][0] == 0.25
    assert vertices.data[1][0] == -0.25
    assert vertices.data[2][1] == 0.25
    assert vertices.data[3][1] == -0.25


def test_quaternion_rotation():
    rotation_axis, angle = np.array([0, 0, 1]), 0.1
    points = np.array(
        [[0.25, 0.0, 0.0], [-0.25, 0.0, 0.0], [0.0, 0.25, 0.0], [0.0, -0.25, 0.0]]
    )
    points_copy = points.copy()
    vertices = Vertices(points)
    rotatable = Quaternion.rotatable(rotation_axis, angle)
    vertices.rotate(rotatable)
    vertices_copy = Vertices(points_copy)
    rotatable = Matrix.rotatable(rotation_axis, angle)
    vertices_copy.rotate(rotatable)
    assert (vertices.data == vertices_copy.data).all()
