from day_04 import is_valid, is_valid_2


def test_problem_1_example_1():
    assert is_valid(111111) is True


def test_problem_1_example_2():
    assert is_valid(223450) is False


def test_problem_1_example_3():
    assert is_valid(123789) is False


def test_problem_2_example_2():
    assert is_valid_2(112233) is True
    assert is_valid_2(123444) is False
    assert is_valid_2(111122) is True


