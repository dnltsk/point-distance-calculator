import pytest

from point_distance_calculator.distance_calculator import calculate_distance
from point_distance_calculator.types import DistanceCalculation, Point


@pytest.fixture
def point_1() -> Point:
    return Point(id=0, lat=40.7128, lon=-74.006)


@pytest.fixture
def point_2() -> Point:
    return Point(id=1, lat=34.0522, lon=-118.2437)


@pytest.fixture
def point_3() -> Point:
    return Point(id=3, lat=51.5074, lon=-0.1278)


def test_calculate_distance(point_1, point_2, point_3):
    result = calculate_distance([point_1, point_2, point_3])

    assert result == [
        DistanceCalculation(
            p1=point_1,
            p2=point_2,
            distance=3935.751690893986,
        ),
        DistanceCalculation(
            p1=point_1,
            p2=point_3,
            distance=5570.229873656523,
        ),
        DistanceCalculation(
            p1=point_2,
            p2=point_3,
            distance=8755.614434910294,
        ),
    ]
