import sys

from anytree import Node, Walker


def read_input(filepath):
    with open(filepath) as f:
        return [line.strip().split(")") for line in f]


def build_tree(input_):
    nodes = {}
    for a, b in input_:
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[b].parent = nodes[a]
    return nodes


def solve1(nodes):
    return sum(n.depth for n in nodes.values())


def solve2(nodes):
    w = Walker()
    paths = w.walk(nodes["YOU"], nodes["SAN"])
    return sum(len(p) for p in paths if isinstance(p, tuple)) - 2


if __name__ == "__main__":
    input_ = read_input("day06.txt")
    nodes = build_tree(input_)
    print(f"Part1: {solve1(nodes)}")
    print(f"Part2: {solve2(nodes)}")
