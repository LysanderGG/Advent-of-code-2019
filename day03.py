from typing import Generator, Iterable, List, Tuple


def read_input(filepath) -> Generator[List[Tuple[str, int]], None, None]:
    with open(filepath) as f:
        for l in f.readlines():
            yield [(x[0], int(x[1:])) for x in l.strip().split(',')]


def compute_wire(coordinates: List[Tuple[str, int]]) -> Generator[Tuple[int, int], None, None]:
    dir_factors = {
        "U": (0, 1),
        "D": (0, -1),
        "L": (-1, 0),
        "R": (1, 0),
    }
    x, y = (0, 0)
    for direction, dist in coordinates:
        dx, dy = dir_factors[direction]
        for _ in range(dist):
            x += dx
            y += dy
            yield (x, y)


def intersection(w1: Iterable[Tuple[int, int]], w2: Iterable[Tuple[int, int]]) -> int:
    intersections = set(w1) & set(w2)
    return min(abs(c[0]) + abs(c[1]) for c in intersections)


def fewest_steps(w1: List[Tuple[int, int]], w2: List[Tuple[int, int]]) -> int:
    intersections = set(w1) & set(w2)
    return min(w1.index(i) + w2.index(i) + 2 for i in intersections)


if __name__ == "__main__":
    c1, c2 = read_input("day03.txt")
    wire_1 = list(compute_wire(c1))
    wire_2 = list(compute_wire(c2))
    print(f"Part1: {intersection(wire_1, wire_2)}")
    print(f"Part2: {fewest_steps(wire_1, wire_2)}")
