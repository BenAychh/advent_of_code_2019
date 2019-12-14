from typing import List, Dict, Callable
from day_05 import handlers, get_parameter_pairs
from itertools import permutations

# New functions, everything was imported from day_05 originally
def handle_3(puzzle_input: List[int], index: int, current_input: int) -> int:
    puzzle_input[puzzle_input[index + 1]] = int(current_input)
    return index + 2


def handle_4(puzzle_input: List[int], index: int) -> int:
    code = str(puzzle_input[index]).rjust(3, '0')
    param_pairs = get_parameter_pairs(code, puzzle_input[index: index + 3])
    return param_pairs[0].get_value(puzzle_input)


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
