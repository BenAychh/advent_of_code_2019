from day_03 import problem_1, problem_2


def test_problem_1_explanation():
    path_1 = "R8,U5,L5,D3"
    path_2 = "U7,R6,D4,L4"
    assert problem_1(path_1, path_2) == 6


def test_problem_1_example_1():
    path_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    path_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert problem_1(path_1, path_2) == 159


def test_problem_1_example_2():
    path_1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    path_2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert problem_1(path_1, path_2) == 135


def test_problem_2_explanation():
    path_1 = "R8,U5,L5,D3"
    path_2 = "U7,R6,D4,L4"
    assert problem_2(path_1, path_2) == 30


def test_problem_2_example_1():
    path_1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
    path_2 = "U62,R66,U55,R34,D71,R55,D58,R83"
    assert problem_2(path_1, path_2) == 610


def test_problem_2_example_2():
    path_1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
    path_2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
    assert problem_2(path_1, path_2) == 410
