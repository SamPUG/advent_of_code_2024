# Advent of code day 1
INPUT_FILE = "inputs\day1.txt"

left_list: list[int] = []
right_dict: dict[int, int] = {}

with open(INPUT_FILE) as input:
    for i, line in enumerate(input):
        line_parts = line.split("   ")
        left_list.append(int(line_parts[0]))

        right_val = int(line_parts[1])
        if right_val in right_dict:
            right_dict[right_val] += 1
        else:
            right_dict[right_val] = 1

    left_list.sort()
    right_list = []
    for item in right_dict.items():
        right_list += [item[0]] * item[1]
    right_list.sort()

    total = 0
    score = 0
    for i in range(len(left_list)):
        total += abs(left_list[i] - right_list[i])

        if left_list[i] in right_dict:
            score += left_list[i] * right_dict[left_list[i]]

    print(f"Total: {total}")
    print(f"Score: {score}")