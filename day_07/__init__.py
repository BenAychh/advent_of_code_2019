from typing import List, Dict, Callable
# from day_05 import handlers, get_parameter_pairs
from itertools import permutations

# ---------------------------- Imported from Day 05 -------------------------
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


# def handle_3(puzzle_input: List[int], index: int) -> int:
#     user_input = input("Enter Input: ")
#     puzzle_input[puzzle_input[index + 1]] = int(user_input)
#     return index + 2
#
#
# def handle_4(puzzle_input: List[int], index: int) -> int:
#     code = str(puzzle_input[index]).rjust(3, '0')
#     param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
#     print("Output: ", param_pairs[0].get_value(puzzle_input))
#     return index + 2


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

# ---------------------------- END Imported from Day 05 -------------------------


# New functions, everything was imported from day_05 originally
def handle_3(puzzle_input: List[int], index: int, current_input: int) -> int:
    puzzle_input[puzzle_input[index + 1]] = int(current_input)
    return index + 2


def handle_4(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(3, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    return param_pairs[0].get_value(puzzle_input)


# Also imported from day 05
handlers: Dict[int, Callable[[List[int], int], int]] = {
    1: handle_1,
    2: handle_2,
    # 3: handle_3,
    # 4: handle_4,
    5: handle_5,
    6: handle_6,
    7: handle_7,
    8: handle_8,
}


def process_amp(puzzle_input: List[int], phase_settings: int, amp_input: int) -> int:
    current_input = phase_settings
    index = 0
    while True:
        int_code = puzzle_input[index]
        if int_code == 99:
            return None
        str_int_code = str(int_code)
        if int_code == 3 or (len(str_int_code) > 2 and int(str_int_code[-2:]) == 3):
            index = handle_3(puzzle_input, index, current_input)
            current_input = amp_input
            continue
        elif int_code == 4 or (len(str_int_code) > 2 and int(str_int_code[-2:]) == 4):
            return handle_4(puzzle_input, index)
        elif int_code in handlers:
            handler = handlers[int_code]
        else:
            final_int = int(str(int_code)[-2:])
            if final_int in handlers:
                handler = handlers[final_int]
            else:
                print(f"unable to find handler for int_code: {int_code} at index: {index}")
                break
        index = handler(puzzle_input, index)


def process_all(puzzle_input: List[int], phase_settings: List[int]) -> int:
    last_output = 0
    for phase_setting in phase_settings:
        last_output = process_amp(puzzle_input, phase_setting, last_output)
    return last_output


def process_all_feedback(puzzle_input: List[int], phase_settings: List[int]) -> int:
    last_output = 0
    while True:
        for phase_setting in phase_settings:
            last_output = process_amp(puzzle_input, phase_setting, last_output)
            if last_output is None:
                break
        else:
            continue
        break
    return last_output


def get_highest(puzzle_input: List[int]) -> (int, List[int]):
    highest = 0
    highest_phase_settings: List[int] = []
    perms = permutations([0, 1, 2, 3, 4])
    for perm in perms:
        phase_results = process_all(puzzle_input, perm)
        if phase_results > highest:
            highest = phase_results
            highest_phase_settings = perm
    return highest, highest_phase_settings


def get_highest_feedback(puzzle_input: List[int]) -> (int, List[int]):
    highest = 0
    highest_phase_settings: List[int] = []
    perms = permutations([5, 6, 7, 8, 9])
    for perm in perms:
        phase_results = process_all_feedback(puzzle_input, perm)
        if phase_results > highest:
            highest = phase_results
            highest_phase_settings = perm
    return highest, highest_phase_settings


if __name__ == '__main__':
    data = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
            -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
            53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]
    # highest, highest_settings = get_highest_feedback(data)
    # print(highest, highest_settings)
    result = process_all_feedback(data, [9, 8, 7, 6, 5])
    print(result)
    # with open('input.txt') as f:
    #     puzzle_input: List[int] = []
    #     for line in f:
    #         for number in line.split(","):
    #             puzzle_input.append(int(number))
    #     part_1_copy = puzzle_input.copy()
    #     print(get_highest(part_1_copy))
