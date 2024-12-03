# Advent of code day 3
import re

INPUT_FILE = "./inputs/day3.txt"

def get_total_str(in_str: str) -> int:
    tot = 0
    for i, j in re.findall(r"mul\((\d*),(\d*)\)", in_str):
        tot += int(i) * int(j)

    return tot


with open(INPUT_FILE) as file:
    file_str = file.read()
    print(f"Total of multiplications part 1: {get_total_str(file_str)}")
    
    # Part 2
    blocks = [dont_block.split('do()') for dont_block in file_str.split("don't()")]
    tot = 0
    # Special case for first block as it will be enabled by default
    tot += get_total_str("".join(blocks[0]))
    for i in range(1, len(blocks)):
        tot += get_total_str("".join(blocks[i][1:]))

    print(f"Total multiplication part 2: {tot}")