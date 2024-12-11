# Advent of code day 10
INPUT_FILE = "inputs/day10.txt"

def find_trail_score(map, x, y, last_val=-1):
    if x < 0 or x >= len(map[0]):
        return []
    if y < 0 or y >= len(map):
        return []
    this_val = map[y][x]

    if this_val == None:
        return []

    if this_val - last_val != 1:
        return []

    if this_val == 9:
        return [(x, y)]
    
    visited_peaks = []

    visited_peaks += find_trail_score(map, x + 1, y, this_val)
    visited_peaks += find_trail_score(map, x - 1, y, this_val)
    visited_peaks += find_trail_score(map, x, y + 1, this_val)
    visited_peaks += find_trail_score(map, x, y - 1, this_val)

    return visited_peaks
    

with open(INPUT_FILE) as input_file:
    trail_map = []
    for line in input_file.readlines():
        int_line = []
        for char in line.strip():
            if char == ".":
                int_line.append(None)
            else:
                int_line.append(int(char))
        trail_map.append(int_line)

    total_1 = 0
    total_2 = 0
    for y in range(len(trail_map)):
        for x in range(len(trail_map[y])):
            if trail_map[y][x] == 0:
                trails = find_trail_score(trail_map, x, y)
                total_1 += len(set(trails))
                total_2 += len(trails)

    print(f"Total score Part 1: {total_1}")
    print(f"Total score Part 2: {total_2}")

