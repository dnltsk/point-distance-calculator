from haversine import haversine

from point_distance_calculator.types import DistanceCalculation, Point


def calculate_distance(points: list[Point]) -> list[DistanceCalculation]:
    distance_calculations = []
    for p1_index, p1 in enumerate(points):
        for p2_index, p2 in enumerate(points[p1_index + 1 :]):
            distance_calculations.append(
                DistanceCalculation(
                    p1=p1,
                    p2=p2,
                    distance=haversine((p1.lat, p1.lon), (p2.lat, p2.lon), unit="km"),
                )
            )
    return distance_calculations
