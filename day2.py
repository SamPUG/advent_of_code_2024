# Advent of code day 2
INPUT_FILE = "inputs\day2.txt"

def is_report_ok(report: list[int]):
    is_increasing = None
    for i in range(1, len(report)):
        diff = report[i] - report[i - 1]

        if diff == 0 or diff > 3  or diff < -3:
            return False
        
        if is_increasing is None:
            is_increasing = diff > 0

        if is_increasing and diff < 0:
            return False

        if not is_increasing and diff > 0:
            return False

    return True
    
def find_safe_levels(input_file, problem_damper = False):
    safe_levels = 0
    for line in input_file:
        report = [int(part) for part in line.split(" ")]
        if is_report_ok(report):
            safe_levels += 1
        elif problem_damper:
            for remove_index in range(0, len(report)):
                this_report = report[:remove_index]
                if remove_index < len(report) - 1:
                    this_report += report[remove_index + 1:]
                if is_report_ok(this_report):
                    safe_levels += 1
                    break
    return safe_levels

with open(INPUT_FILE) as input_file:
    safe_levels = find_safe_levels(input_file)
    print(f"Safe levels (no dampener): {safe_levels}")
    input_file.seek(0)
    safe_levels = find_safe_levels(input_file, True)
    print(f"Safe levels (with dampener): {safe_levels}")