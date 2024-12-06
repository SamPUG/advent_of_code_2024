# Advent of code day 4
INPUT_FILE = "./inputs/day4.txt"
SEARCH_WORD = "XMAS"

def has_xmas(input: list[str], start_x: int, start_y: int, x_step: int, y_step: int) -> bool:
    x = start_x
    y = start_y

    for i in range(len(SEARCH_WORD)):
        if y < 0 or y >= len(input): return False
        if x < 0 or x >= len(input[y]): return False
        if input[y][x] != SEARCH_WORD[i]: return False

        x += x_step
        y += y_step
   
    return True

def has_cross_mass(input: list[str], x: int, y: int) -> bool:
    if input[y][x] != "A": return False
    if x < 1 or x > len(input[0]) - 2: return False
    if y < 1 or y > len(input) - 2: return False

    diag = input[y-1][x-1] + input[y][x] + input[y+1][x+1]
    if diag != "MAS" and diag != "SAM": return False
    diag = input[y+1][x-1] + input[y][x] + input[y-1][x+1]
    if diag != "MAS" and diag != "SAM": return False

    return True



with open(INPUT_FILE) as input_file:
    input = input_file.readlines()

    total_xmas = 0
    total_crossmass = 0
    for y in range(len(input)):
        for x in range(len(input[y])):
            total_crossmass += 1 if has_cross_mass(input, x, y) else 0
            for i in range (-1, 2):
                for j in range(-1, 2):
                    total_xmas += 1 if has_xmas(input, x, y, i, j) else 0

    print(f"Total Part 1 {total_xmas}")
    print(f"Total Part 2 {total_crossmass}")
          
