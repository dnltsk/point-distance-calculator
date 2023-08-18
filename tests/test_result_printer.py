from _pytest.capture import CaptureFixture

from point_distance_calculator.result_printer import print_result
from point_distance_calculator.types import DistanceCalculation


def test_print_result(
    capsys: CaptureFixture, c1: DistanceCalculation, c2: DistanceCalculation
):
    print_result([c1, c2])
    captured = capsys.readouterr()
    assert captured.out == (
        "\n"
        "Pairwise Distances (in km):\n"
        "Point 0 to Point 1: 42.1\n"
        "Point 0 to Point 3: 999.7\n"
    )
