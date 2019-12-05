from typing import Dict


def problem_1(start: int, end: int) -> int:
    count = 0
    for n in range(start, end + 1):
        if is_valid(n):
            count += 1
    return count


def problem_2(start: int, end: int) -> int:
    count = 0
    for n in range(start, end + 1):
        if is_valid_2(n):
            count += 1
    return count


def is_valid(number: int) -> bool:
    as_string = int_to_string_array(number)
    return len(as_string) == 6 and has_adjacent_same(as_string) and is_never_decreasing(as_string)


def is_valid_2(number: int) -> bool:
    as_string = int_to_string_array(number)
    return len(as_string) == 6 and has_groups_of_two_adjacent_same_(as_string) and is_never_decreasing(as_string)


def has_adjacent_same(number: str) -> bool:
    for i in range(len(number) - 1):
        if number[i] == number[i + 1]:
            return True
    return False


def has_groups_of_two_adjacent_same_(number: str) -> bool:
    digit_counts: Dict[str, int] = {}
    for i in range(len(number)):
        if number[i] not in digit_counts:
            digit_counts[number[i]] = 0
        digit_counts[number[i]] += 1
    for count in digit_counts.values():
        if count == 2:
            return True


def is_never_decreasing(number: str) -> bool:
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return False
    return True


def int_to_string_array(number: int) -> str:
    return str(number)


input_start = 236491
input_end = 713787

if __name__ == '__main__':
    print("Problem 1: ", problem_1(input_start, input_end))

    print("Problem 2: ", problem_2(input_start, input_end))
