def read_input(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readline().split(",")]


def solve(input, noun, verb):
    input[1] = noun
    input[2] = verb

    current_op = 0
    while (op := input[current_op]) != 99:
        x, y, dist = input[current_op+1:current_op+4]
        if op == 1:
            input[dist] = input[x] + input[y]
        elif op == 2:
            input[dist] = input[x] * input[y]
        current_op += 4

    return input[0]


def solve2(input, target_val):
    for noun in range(100):
        for verb in range(100):
            res = solve(list(input), noun, verb)
            if res == target_val:
                return 100 * noun + verb


if __name__ == "__main__":
    input = read_input("day02.txt")
    print(f"Part1: {solve(input, 12, 2)}")

    input = read_input("day02.txt")
    print(f"Part2: {solve2(input, 19690720)}")
