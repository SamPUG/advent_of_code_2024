# Advent of code day 6
# Needed a hint for part 2
INPUT_FILE = "./inputs/day6.txt"


def find_visited_positions(floor_plan: list[str], start_x, start_y) -> set[(int, int, int)]:
    x = start_x 
    y = start_y
    visited_positions: set[(int, int, int)] = set()

    direction_x = 0
    direction_y = -1

    while True:
        next_x = x + direction_x
        next_y = y + direction_y
        
        visited_position = (x, y, direction_x * 2 + direction_y)
        if next_x < 0 or next_x == len(floor_plan[0]) or next_y < 0 or next_y == len(floor_plan):
            visited_positions.add(visited_position)
            return visited_positions
        elif floor_plan[next_y][next_x] == "#":
            if direction_x == 0:
                direction_x = direction_y * -1
                direction_y = 0
            else:
                direction_y = direction_x
                direction_x = 0
        else:
            if visited_position in visited_positions:
                return None
        
            visited_positions.add(visited_position)
            x = next_x
            y = next_y
        

with open(INPUT_FILE) as input_file:

    start_x = -1
    start_y = -1
    floor_plan: list[str] = []
    visited_positions = set()

    for i, line in enumerate(input_file):
        floor_plan.append(line.strip())
        if start_x < 0:
            start_x = line.find("^")
            start_y = i

    visited_positions = set([(pos[0], pos[1]) for pos in find_visited_positions(floor_plan, start_x, start_y)])
    print(f"Part 1: {len(visited_positions)}")

    floor_plan_cpy = floor_plan.copy()

    possible_loops = 0
    for obsticle_pos in [pos for pos in visited_positions if pos[0] != start_x or pos[1] != start_y]:
        floor_plan[obsticle_pos[1]] = floor_plan[obsticle_pos[1]][:obsticle_pos[0]] + "#" + floor_plan[obsticle_pos[1]][obsticle_pos[0] + 1:]

        floor_plan_cpy[obsticle_pos[1]] = floor_plan_cpy[obsticle_pos[1]][:obsticle_pos[0]] + "O" + floor_plan_cpy[obsticle_pos[1]][obsticle_pos[0] + 1:]

        if find_visited_positions(floor_plan, start_x, start_y) is None:
            possible_loops += 1

        floor_plan[obsticle_pos[1]] = floor_plan[obsticle_pos[1]][:obsticle_pos[0]] + "." + floor_plan[obsticle_pos[1]][obsticle_pos[0] + 1:]

    print(f"Part 2: {possible_loops}")


    






