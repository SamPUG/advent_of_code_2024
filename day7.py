from typing import Generator

INPUT_FILE = "inputs/day7.txt"

def operator_generator(length, with_concat = False, current="") -> Generator[str, None, None]:
    if len(current) == length:
        yield current
    else:
        if with_concat:
            yield from operator_generator(length, with_concat, current + "|")
        yield from operator_generator(length, with_concat, current + "+")
        yield from operator_generator(length, with_concat, current + "*")


def calculate_input(input_str: str) -> int:
    total = 0

    val = ""
    operator = ""
    for i in range(len(input_str) + 1):
        char = "+"  # To make sure we deal with the last val, operator doesn't matter, just want to trigger the operator behaviour
        if i < len(input_str):
            char = input_str[i]

        if char not in ["+", "*", "|"]:
            val += char
        else:
            int_val = int(val)
            if operator == "+":
                total += int_val
            elif operator == "*":
                total *= int_val
            elif operator == "|":
                total = int(str(total) + val)
            else:
                operator = char
                total += int_val
            operator = char
            val = ""

    return total


def can_produce_target(vals: list[int], target: int, with_concat = False) -> bool:
    # print(f"Target: {target}")
    for operator_set in operator_generator(len(vals) -1, with_concat):
        test_str = ""
        for i, val in enumerate(vals):
            test_str += str(val)
            if i < len(operator_set):
                test_str += operator_set[i]

        calc_total = calculate_input(test_str)
        if calc_total == target:
            return True

    return False


with open(INPUT_FILE) as input_file:
    not_possible_ref = set()
    with open("not_possible_help.txt") as help_file:
        for line in help_file:
            not_possible_ref.add(line.strip())

    with open("not_possible_missing.txt", "w") as output_file:
    
        total = 0
        total_2 = 0
        for line in input_file:
            # print(line)
            parts = line.split(":")

            target = int(parts[0])
            vals = [int(val) for val in parts[1].strip().split(" ")]
            last_total_2 = total_2

            if can_produce_target(vals, target):
                total += target
                total_2 += target
            elif can_produce_target(vals, target, True):
                total_2 += target
            elif not line.strip() in not_possible_ref:
                output_file.write(line)

    print(f"Total part 1: {total}")
    print(f"Total part 2: {total_2}")
