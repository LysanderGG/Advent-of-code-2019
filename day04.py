from collections import Counter

if __name__ == "__main__":
    numbers = [s for s in map(str, range(264793, 803935 + 1)) if sorted(s) == list(s)]
    print(f"Part1: {sum(len(s) > len(set(s)) for s in numbers)}")
    print(f"Part2: {sum(2 in Counter(s).values() for s in numbers)}")
