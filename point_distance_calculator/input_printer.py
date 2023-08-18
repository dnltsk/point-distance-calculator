from point_distance_calculator.types import Point


def print_input(points: list[Point]) -> None:
    print("\nInput Points:")
    for point in points:
        print(
            f"Point {point.id}: "
            f"Latitude {round(point.lat, 4)}, "
            f"Longitude {round(point.lon, 4)}"
        )
