from point_distance_calculator.point_generator import generate_points


def main():
    points = generate_points()
    print(f"{points=}")


if __name__ == "__main__":
    main()
