# Advent of code day 9
INPUT_FILE = "inputs/day9.txt"

def part_1(disk_map_str: str) -> int:
    disk_map = [int(char) for char in disk_map_str]
    left_index = 0
    right_index = len(disk_map) - 1
    left_file_id = 0
    right_file_id = int((len(disk_map) - 1) / 2)
    checksum = 0
    inserted_count = 0

    while left_index <= right_index:
        if left_index % 2 == 0:
            if disk_map[left_index] > 0:
                checksum += left_file_id * inserted_count
                inserted_count += 1
                disk_map[left_index] -= 1
            else:
                left_index += 1
                left_file_id += 1
        else:
            if disk_map[right_index] > 0:
                if disk_map[left_index] > 0:
                    checksum += right_file_id * inserted_count
                    inserted_count += 1
                    disk_map[right_index] -= 1
                    disk_map[left_index] -= 1
                else:
                    left_index += 1
            else:
                right_index -= 2
                right_file_id -=1

    return checksum

def part_2(disk_str_map: str) -> int:
    file_index = 0
    disk_map = []
    for file_index, i in enumerate(range(0, len(disk_str_map), 2)):
        disk_map += [file_index] * int(disk_str_map[i])
        if i + 1 < len(disk_str_map):
            disk_map += [None] * int(disk_str_map[i + 1])

    move_group_right = move_group_left = len(disk_map) - 1
    while move_group_left > 0:
        if disk_map[move_group_right] == None:
            move_group_right -= 1
            move_group_left -= 1
        elif disk_map[move_group_left] == disk_map[move_group_right]:
            move_group_left -= 1
        else:
            # Try to find a space for the being moved
            location_group_left = location_group_right = 0
            while location_group_right <= move_group_left + 1:
                if disk_map[location_group_left] != None:
                    location_group_left += 1
                    location_group_right = location_group_left
                elif (location_group_right - location_group_left) == (move_group_right - move_group_left):
                    # Can move into this space
                    part1 = disk_map[:location_group_left]
                    part2 = disk_map[move_group_left + 1: move_group_right + 1]
                    part3 = disk_map[location_group_right: move_group_left + 1]
                    part4 = [None] * (move_group_right - move_group_left)
                    part5 = disk_map[move_group_right + 1:]

                    disk_map =  part1 + part2 + part3 + part4 + part5
                    move_group_left = move_group_right
                    break
                elif disk_map[location_group_right] != None:
                    location_group_left = location_group_right
                else:
                    location_group_right += 1

            move_group_right = move_group_left

    checksum = 0
    for i, val in enumerate(disk_map):
        if val is not None:
            checksum += i * val
     
    return checksum


with open(INPUT_FILE) as input_file:
    drive_map = input_file.read().strip()
    print(f"Part 1 Checksum: {part_1(drive_map)}")
    print(f"Part 2 Checksum: {part_2(drive_map)}")

