from typing import List, Dict, Callable


class ValueAndParamPair:
    index: int
    parameter: int

    def __init__(self, index: int, parameter: int):
        self.index = index
        self.parameter = parameter

    def get_value(self, puzzle_input: List[int]) -> int:
        if self.parameter == 0:
            return puzzle_input[self.index]
        return self.index


def get_parameter_pairs(int_code: str, int_code_slice: List[int]) -> List[ValueAndParamPair]:
    params = int_code[0:len(int_code) - 2]
    params = params[len(params)::-1]
    pairs: List[ValueAndParamPair] = []
    for i in range(len(params)):
        pairs.append(ValueAndParamPair(int_code_slice[i+1], int(params[i])))
    return pairs


def handle_1(puzzle_input: List[int], index: int) -> int:
    code: str = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    puzzle_input[puzzle_input[index + 3]] = value1 + value2
    return index + 4


def handle_2(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    puzzle_input[puzzle_input[index + 3]] = value1 * value2
    return index + 4


def handle_3(puzzle_input: List[int], index: int) -> int:
    user_input = input("Enter Input: ")
    puzzle_input[puzzle_input[index + 1]] = int(user_input)
    return index + 2


def handle_4(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(3, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    print("Output: ", param_pairs[0].get_value(puzzle_input))
    return index + 2


def handle_5(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(4, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    value = param_pairs[0].get_value(puzzle_input)
    if value != 0:
        return param_pairs[1].get_value(puzzle_input)
    return index + 3


def handle_6(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(4, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    if param_pairs[0].get_value(puzzle_input) == 0:
        return param_pairs[1].get_value(puzzle_input)
    return index + 3


def handle_7(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    if value1 < value2:
        puzzle_input[puzzle_input[index + 3]] = 1
    else:
        puzzle_input[puzzle_input[index + 3]] = 0
    return index + 4


def handle_8(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(5, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 4])
    value1 = param_pairs[0].get_value(puzzle_input)
    value2 = param_pairs[1].get_value(puzzle_input)
    if value1 == value2:
        puzzle_input[puzzle_input[index + 3]] = 1
    else:
        puzzle_input[puzzle_input[index + 3]] = 0
    return index + 4


handlers: Dict[int, Callable[[List[int], int], int]] = {
    1: handle_1,
    2: handle_2,
    3: handle_3,
    4: handle_4,
    5: handle_5,
    6: handle_6,
    7: handle_7,
    8: handle_8,
}


def process(puzzle_input: List[int]) -> None:
    index = 0
    while True:
        int_code = puzzle_input[index]
        if int_code == 99:
            break
        if int_code in handlers:
            handler = handlers[int_code]
        else:
            final_int = int(str(int_code)[-2:])
            if final_int in handlers:
                handler = handlers[final_int]
            else:
                print(f"unable to find handler for int_code: {int_code} at index: {index}")
                break
        index = handler(puzzle_input, index)


if __name__ == '__main__':
    with open('input.txt') as f:
        puzzle_input: List[int] = []
        for line in f:
            for number in line.split(","):
                puzzle_input.append(int(number))
        part_1_copy = puzzle_input.copy()
        process(part_1_copy)

