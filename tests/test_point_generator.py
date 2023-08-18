from unittest import mock
from unittest.mock import MagicMock

from point_distance_calculator.point_generator import generate_points
from point_distance_calculator.types import Point


@mock.patch(
    "point_distance_calculator.point_generator.np.random.uniform", autospec=True
)
def test_generated_points_are_random(uniform_mock: MagicMock):
    uniform_mock.side_effect = uniform_side_effect

    result = generate_points()

    assert len(result) == 5
    for index, point in enumerate(result):
        assert point == Point(
            id=index,
            lat=52.5,
            lon=13.5,
        )


def uniform_side_effect(*args: list[float]) -> float:
    if args[0] == -180 and args[1] == 180:
        return 13.5
    elif args[0] == -90 and args[1] == 90:
        return 52.5
    else:
        raise ValueError(f"Unexpected arguments: {args}")
