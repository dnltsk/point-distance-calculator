import numpy as np

from point_distance_calculator.types import Point


def generate_points() -> list[Point]:
    points = []
    for i in range(5):
        points.append(
            Point(
                id=i, lon=np.random.uniform(-180, 180), lat=np.random.uniform(-90, 90)
            )
        )
    return points
