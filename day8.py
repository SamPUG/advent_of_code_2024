# Advent of code day 8
import numpy as np
INPUT_FILE = "inputs/day8.txt"

def is_in_bounds(vector: np.array, x_max: int, y_max: int) -> bool:
    for i, max in enumerate([x_max, y_max]):
        if vector[i] < 0 or vector[i] > max:
            return False
    return True


def get_anti_nodes_before_boundary(current_tower: np.array, vector: np.array, map_width: int, map_length: int) -> list[np.array]:
    anti_nodes = []
    magnitude = 1
    while True:
        anti_node = current_tower + vector * magnitude
        if is_in_bounds(anti_node, map_width, map_length):
            anti_nodes.append(anti_node)
            magnitude += 1
        else:
            return anti_nodes


with open(INPUT_FILE) as input_file:
    towers = {}
    for i, line in enumerate(input_file):
        for j, val in enumerate(line.strip()):
            if val == ".": continue
            if val in towers:
                towers[val].append(np.array([j, i]))
            else:
                towers[val] = [np.array([j, i])]

    map_width = j
    map_length = i

    anti_node_positions = set()
    anti_node_positions_harmonics = set()
    for tower_type in towers:
        current_towers = towers[tower_type]

        for i in range(len(current_towers) - 1):
            for j in range(i + 1, len(current_towers)):
                # Get the vector between the two towers
                vector = current_towers[i] - current_towers[j]

                magnitude = np.linalg.norm(vector)
                normalized_vector = vector / magnitude

                mag_norm = np.linalg.norm(normalized_vector)
                if np.isclose(mag_norm, 1, atol=1e-9):
                    # Only consider diags, horizontal or vertial
                    anti_nodes = get_anti_nodes_before_boundary(current_towers[j], vector, map_width, map_length)
                    if len(anti_nodes) > 1:
                        anti_node = anti_nodes.pop(1)
                        anti_node_positions.add((anti_node[0], anti_node[1]))

                    anti_node_positions_harmonics = anti_node_positions_harmonics.union(set([(an[0], an[1]) for an in anti_nodes]))

                    anti_nodes = get_anti_nodes_before_boundary(current_towers[i], vector * -1, map_width, map_length)
                    if len(anti_nodes) > 1:
                        anti_node = anti_nodes.pop(1)
                        anti_node_positions.add((anti_node[0], anti_node[1]))

                    anti_node_positions_harmonics = anti_node_positions_harmonics.union(set([(an[0], an[1]) for an in anti_nodes]))


    print(f"No anti nodes: {len(anti_node_positions)}")
    print(f"No anti nodes with harmonics: {len(anti_node_positions.union(anti_node_positions_harmonics))}")

    input_file.seek(0)
    with open("out_map.txt", "w") as outmap:
        for i, line in enumerate(input_file):
            for j, char in enumerate(line):
                if (j, i) in anti_node_positions.union(anti_node_positions_harmonics):
                    char = "#"  
                outmap.write(char)



