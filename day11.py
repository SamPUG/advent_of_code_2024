INPUT_FILE = "inputs/day11.txt"

def run_rules(vals: list[int], remaining_blinks, precompute_table = {}) -> int:
    remaining_blinks -= 1
    if remaining_blinks < 0:
        return len(vals)
    
    total = 0
    for val in vals:
        this_total = 0

        if val in precompute_table and remaining_blinks in precompute_table[val]:
            this_total = precompute_table[val][remaining_blinks]
        else:
            if val == 0:
                this_total += run_rules([1], remaining_blinks)
            elif len(str(val)) % 2 == 0:
                str_val = str(val)
                this_total += run_rules([int(str_val[:int(len(str_val) / 2)]), int(str_val[int(len(str_val) / 2):])], remaining_blinks)
            else:
                this_total += run_rules([val * 2024], remaining_blinks)

            # Add to precompute
            if val in precompute_table:
                precompute_table[val][remaining_blinks] = this_total
            else:
                precompute_table[val] = {remaining_blinks: this_total}
        total += this_total
    
    return total

with open(INPUT_FILE) as input_file:
    vals = [int(val) for val in input_file.read().strip().split(" ")]
    total = run_rules(vals, 25)
    print(f"Total stones, 25 blinks: {total}")
    total = run_rules(vals, 75)
    print(f"Total stones, 75 blinks: {total}")