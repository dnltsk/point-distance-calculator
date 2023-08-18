from unittest import mock
from unittest.mock import MagicMock

from point_distance_calculator.main import main
from point_distance_calculator.types import DistanceCalculation, Point


@mock.patch("point_distance_calculator.main.generate_points", autospec=True)
@mock.patch("point_distance_calculator.main.print_input", autospec=True)
@mock.patch("point_distance_calculator.main.calculate_distance", autospec=True)
@mock.patch("point_distance_calculator.main.print_result", autospec=True)
def test_main(
    print_result: MagicMock,
    calculate_distance: MagicMock,
    print_input: MagicMock,
    generate_points: MagicMock,
    p1: Point,
    p2: Point,
    c1: DistanceCalculation,
):
    # given
    given_points = [p1, p2]
    generate_points.return_value = given_points

    given_calculations = [c1]
    calculate_distance.return_value = given_calculations

    # when
    main()

    # then
    generate_points.assert_called_once()
    print_input.assert_called_once_with(given_points)
    calculate_distance.assert_called_once_with(given_points)
    print_result.assert_called_once_with(given_calculations)
