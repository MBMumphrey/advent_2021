import sys

if __name__ == "__main__":
    problem_input = sys.argv[1]

    #Count the number of times 1, 4, 7, 8 appear in output
    #This is the number of times values appear with 2, 3, 4, or 7 elements
    count = 0
    with open(problem_input, 'r') as f:
        for line in f:
            output = line.split("|")[1].strip().split()
            for x in output:
                if len(x) in [2, 3, 4, 7]:
                    count += 1

    print(count)
