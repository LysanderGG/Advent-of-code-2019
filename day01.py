def read_input(filepath):
    with open(filepath) as f:
        return [int(line) for line in f]


def solve(input):
    return sum(i // 3 - 2 for i in input)


def solve2(input):
    sum = 0
    for i in input:
        while (f := (i // 3 - 2)) > 0:
            sum += f
            i = f
    return sum


if __name__ == "__main__":
    input = read_input("day01.txt")
    print(f"Part1: {solve(input)}")
    print(f"Part2: {solve2(input)}")
