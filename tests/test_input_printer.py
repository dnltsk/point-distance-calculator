from _pytest.capture import CaptureFixture

from point_distance_calculator.input_printer import print_input
from point_distance_calculator.types import Point


def test_print_input(capsys: CaptureFixture, p1: Point, p2: Point):
    print_input([p1, p2])
    captured = capsys.readouterr()
    assert captured.out == (
        "\n"
        "Input Points:\n"
        "Point 0: Latitude 40.7128, Longitude -74.006\n"
        "Point 1: Latitude 34.0522, Longitude -118.2437\n"
    )
