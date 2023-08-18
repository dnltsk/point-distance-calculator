from point_distance_calculator.types import DistanceCalculation


def print_result(calcs: list[DistanceCalculation]) -> None:
    print("\nPairwise Distances (in km):")
    for calc in calcs:
        print(f"Point {calc.p1.id} to Point {calc.p2.id}: {round(calc.distance, 1)}")
