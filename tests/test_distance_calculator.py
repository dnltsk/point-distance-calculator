from point_distance_calculator.distance_calculator import calculate_distance
from point_distance_calculator.types import DistanceCalculation, Point


def test_calculate_distance(p1: Point, p2: Point, p3: Point):
    result = calculate_distance([p1, p2, p3])

    assert result == [
        DistanceCalculation(
            p1=p1,
            p2=p2,
            distance=3935.751690893986,
        ),
        DistanceCalculation(
            p1=p1,
            p2=p3,
            distance=5570.229873656523,
        ),
        DistanceCalculation(
            p1=p2,
            p2=p3,
            distance=8755.614434910294,
        ),
    ]
