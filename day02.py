def read_input(filepath):
    with open(filepath) as f:
        return [int(x) for x in f.readline().split(",")]


def solve(program, noun, verb):
    program = list(program)
    program[1] = noun
    program[2] = verb

    current_op = 0
    while (op := program[current_op]) != 99:
        x, y, dist = program[current_op+1:current_op+4]
        if op == 1:
            program[dist] = program[x] + program[y]
        elif op == 2:
            program[dist] = program[x] * program[y]
        else:
            raise ValueError(f"Unknown instruction {op=}")
        current_op += 4

    return program[0]


def solve2(program, target_val):
    for noun in range(100):
        for verb in range(100):
            res = solve(program, noun, verb)
            if res == target_val:
                return 100 * noun + verb


if __name__ == "__main__":
    program = read_input("day02.txt")
    print(f"Part1: {solve(program, 12, 2)}")
    print(f"Part2: {solve2(program, 19690720)}")
