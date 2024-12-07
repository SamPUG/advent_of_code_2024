# Advent of code day 5
INPUT_FILE = "./inputs/day5.txt"


# Return -1 if invalid. Midpoint if valid
def check_line(pages: list[int], rules: dict[int, list[int]]) -> bool:
    past_vals = set()
    forbidden_vals = set()
    for page in pages:
        if page in forbidden_vals: return False

        if page in rules:
            for val in rules[page]:
                if val not in past_vals:
                    forbidden_vals.add(val)
        
    return True


def fix_order(pages: list[int], rules: dict[int, list[int]]) -> list[int]:

    if check_line(pages, rules):
        return pages
    
    check_page = pages.pop(int((len(pages) - 1) / 2))

    before_pages = []
    i = 0
    while i < len(pages):
        if pages[i] in rules[check_page]:
            before_pages.append(pages.pop(i))
        else:
            i += 1
    
    return fix_order(before_pages, rules) + fix_order([check_page] + pages, rules)


with open(INPUT_FILE) as input_file:
    # Read rules into dict which contains all numbers which should come before the key
    rule_dict: dict[int, list[int]] = {}
    while True:
        line = input_file.readline().strip()
        if len(line) == 0:
            break
        parts = [int(part) for part in line.split("|")]
    
        if parts[1] in rule_dict:
            rule_dict[parts[1]].append(parts[0])
        else:
            rule_dict[parts[1]] = [parts[0]]

    total = 0
    total_2 = 0
    for line in input_file.readlines():
        line_parts = [int(page) for page in line.split(",")]
        
        fixed_pages = fix_order(line_parts.copy(), rule_dict)
        midpoint_val = fixed_pages[int((len(fixed_pages) - 1) / 2)]

        if fixed_pages == line_parts:
            total += midpoint_val
        else:
            total_2 += midpoint_val


    print(f"Total part 1: {total}")
    print(f"Total part 2: {total_2}")