from point_distance_calculator.distance_calculator import calculate_distance
from point_distance_calculator.point_generator import generate_points


def main():
    points = generate_points()
    print(f"{points=}")
    result = calculate_distance(points)
    print(f"{result=}")


if __name__ == "__main__":
    main()
