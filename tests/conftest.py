import pytest

from point_distance_calculator.types import Point


@pytest.fixture
def p1() -> Point:
    return Point(id=0, lat=40.7128, lon=-74.006)


@pytest.fixture
def p2() -> Point:
    return Point(id=1, lat=34.0522, lon=-118.2437)


@pytest.fixture
def p3() -> Point:
    return Point(id=3, lat=51.5074, lon=-0.1278)
