from day_01 import calculate_fuel, calculate_fuel_with_fuel


def test_example_one():
    data = 12
    result = calculate_fuel(data)
    assert result == 2


def test_example_two():
    assert calculate_fuel(14) == 2


def test_example_three():
    assert calculate_fuel(1969) == 654


def test_example_four():
    assert calculate_fuel(100756) == 33583


def test_part_2_example_one():
    assert calculate_fuel_with_fuel(14) == 2


def test_part_2_example_two():
    assert calculate_fuel_with_fuel(1969) == 966


def test_part_2_example_three():
    assert calculate_fuel_with_fuel(100756) == 50346
