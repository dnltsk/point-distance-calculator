from point_distance_calculator.distance_calculator import calculate_distance
from point_distance_calculator.input_printer import print_input
from point_distance_calculator.point_generator import generate_points
from point_distance_calculator.result_printer import print_result


def main():
    points = generate_points()
    print_input(points)
    result = calculate_distance(points)
    print_result(result)


if __name__ == "__main__":
    main()
