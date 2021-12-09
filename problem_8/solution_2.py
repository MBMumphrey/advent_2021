import sys

def unscramble(digits):
    wire_map = {}
    digit_sets = {k:[] for k in range(10)}

    #Identify unique values 1, 4, 7, 8
    for digit in digits:
        if len(digit) == 2:
            digit_sets[1] = set([c for c in digit])
        elif len(digit) == 3:
            digit_sets[7] = set([c for c in digit])
        elif len(digit) == 4:
            digit_sets[4] = set([c for c in digit])
        elif len(digit) == 7:
            digit_sets[8] = set([c for c in digit])

    #Identify 6 as the only len 6 segment not containing all elements of 1
    for digit in digits:
        digit_set = set([c for c in digit])
        if len(digit) == 6 and not digit_sets[1].issubset(digit_set):
            digit_sets[6] = digit_set

    #Identify 9 as the only len 6 segment containing all elements of 4
    for digit in digits:
        digit_set = set([c for c in digit])
        if len(digit) == 6 and digit_sets[4].issubset(digit_set):
            digit_sets[9] = digit_set
    
    #Identify 0 as the only remaining len 6 segment
    for digit in digits:
        digit_set = set([c for c in digit])
        if len(digit) == 6 and not digit_set in [digit_sets[6], digit_sets[9]]:
            digit_sets[0] = digit_set

    #Identify "a" as the difference from 1 and 7
    wire_map["a"] = (digit_sets[7] - digit_sets[1]).pop()

    #Identify "d", "c", "e" as the missing elements from 0, 6, 9
    wire_map["d"] = (digit_sets[8] - digit_sets[0]).pop()
    wire_map["c"] = (digit_sets[8] - digit_sets[6]).pop()
    wire_map["e"] = (digit_sets[8] - digit_sets[9]).pop()

    #Identify "f" as the element of 7 that is not "a" or "c"
    wire_map["f"] = (digit_sets[7] - set([wire_map["a"], wire_map["c"]])).pop()

    #Identify "b" as the element of 4 that does not match "c", "d", "f"
    wire_map["b"] = (digit_sets[4] - set([wire_map["c"], wire_map["d"], wire_map["f"]])).pop()

    #Identify "g" as the final element
    wire_map["g"] = (digit_sets[8] - set([x for x in wire_map.values()])).pop()

    return wire_map

def decode(wire_map, values):
    display_sets = {
        0:set([wire_map[x] for x in ["a", "b", "c", "e", "f", "g"]]),
        1:set([wire_map[x] for x in ["c", "f"]]),
        2:set([wire_map[x] for x in ["a", "c", "d", "e", "g"]]),
        3:set([wire_map[x] for x in ["a", "c", "d", "f", "g"]]),
        4:set([wire_map[x] for x in [ "b", "c", "d", "f"]]),
        5:set([wire_map[x] for x in ["a", "b", "d", "f", "g"]]),
        6:set([wire_map[x] for x in ["a", "b", "d", "e", "f", "g"]]),
        7:set([wire_map[x] for x in ["a", "c", "f"]]),
        8:set([wire_map[x] for x in ["a", "b", "c", "d", "e", "f", "g"]]),
        9:set([wire_map[x] for x in ["a", "b", "c", "d", "f", "g"]])
    }

    real_value = ""
    for value in values:
        value_set = set([c for c in value])
        real_value += [f"{i}" for i, x in enumerate(display_sets.values()) if x == value_set][0]

    return int(real_value)

if __name__ == "__main__":
    problem_input = sys.argv[1]

    total = 0
    with open(problem_input, 'r') as f:
        for line in f:
            line = line.split("|")
            digits = line[0].strip().split()
            output = line[1].strip().split()

            wire_map = unscramble(digits)
            total += decode(wire_map, output)

    print(total)

            