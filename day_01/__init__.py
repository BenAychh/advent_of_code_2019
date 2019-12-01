import math


def calculate_fuel(weight: int) -> int:
    return math.floor(weight / 3) - 2


def calculate_fuel_with_fuel(weight: int) -> int:
    total_fuel = 0
    while weight > 0:
        weight = max(calculate_fuel(weight), 0)
        total_fuel += weight
    return total_fuel


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