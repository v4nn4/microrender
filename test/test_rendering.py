from microrender.point import Point
from microrender.render import Window
from microrender.vertices import Vertices


def test_rendering():
    window = Window(50, 50)
    vertices = Vertices(
        [
            Point(0.25, 0.0, 0.0),
            Point(-0.25, 0.0, 0.0),
            Point(0.0, 0.25, 0.0),
            Point(0.0, -0.25, 0.0),
        ]
    )
    image = window.render(vertices)
    assert image
    axis = Point(0, 0, 1)
    angle = 0.1
    vertices.rotate(axis, angle)
    image = window.render(vertices)
    assert image