import math


def calculate_fuel(weight: int) -> int:
    return math.floor(weight / 3) - 2


def calculate_fuel_with_fuel(weight: int) -> int:
    fuel = math.floor(weight / 3) - 2
    return fuel + calculate_fuel_with_fuel(fuel) if fuel > 0 else 0


if __name__ == '__main__':
    with open('input.txt') as f:
        total_weight: int = 0
        for item in f:
            total_weight += calculate_fuel(int(item))
        print("part 1:", total_weight)

    with open('input.txt') as f:
        total_weight = 0
        for item in f:
            total_weight += calculate_fuel_with_fuel(int(item))
        print("part 2:", total_weight)