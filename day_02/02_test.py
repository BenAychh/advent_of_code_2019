from day_02 import problem_1


def test_problem_1_example_one():
    assert problem_1([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]


def test_problem_1_example_two():
    assert problem_1([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]


def test_problem_1_example_three():
    assert problem_1([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]


def test_problem_1_example_four():
    assert problem_1([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]
