from typing import List, Dict

functions: Dict[int, lambda a, b: int] = {1: lambda a, b: a + b, 2: lambda a, b: a * b}


def problem_1(int_code: List[int]) -> List[int]:
    copy = int_code.copy()
    for i in range(len(copy))[::4]:
        op_code = copy[i]
        if op_code == 99:
            break
        p1 = copy[copy[i + 1]]
        p2 = copy[copy[i + 2]]
        calculated_value = functions[op_code](p1, p2)
        copy[copy[i + 3]] = calculated_value
    return copy


problem_input = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 10, 19, 1, 19, 5, 23, 2, 23, 6, 27, 1, 27, 5,
                 31, 2, 6, 31, 35, 1, 5, 35, 39, 2, 39, 9, 43, 1, 43, 5, 47, 1, 10, 47, 51, 1, 51, 6, 55, 1, 55, 10,
                 59, 1, 59, 6, 63, 2, 13, 63, 67, 1, 9, 67, 71, 2, 6, 71, 75, 1, 5, 75, 79, 1, 9, 79, 83, 2, 6, 83,
                 87, 1, 5, 87, 91, 2, 6, 91, 95, 2, 95, 9, 99, 1, 99, 6, 103, 1, 103, 13, 107, 2, 13, 107, 111, 2,
                 111, 10, 115, 1, 115, 6, 119, 1, 6, 119, 123, 2, 6, 123, 127, 1, 127, 5, 131, 2, 131, 6, 135, 1, 135,
                 2, 139, 1, 139, 9, 0, 99, 2, 14, 0, 0]
if __name__ == '__main__':
    working_copy = problem_input.copy()
    working_copy[1] = 12
    working_copy[2] = 2
    print("Part 1:", problem_1(working_copy)[0])

    for x1 in range(100):
        for x2 in range(100):
            working_copy = problem_input.copy()
            working_copy[1] = x1
            working_copy[2] = x2
            calc = problem_1(working_copy)
            if calc[0] == 19690720:
                break
        else:
            continue
        break
    print("Part 2:", working_copy[1:3])
