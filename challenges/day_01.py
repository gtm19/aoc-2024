from collections import Counter
from pathlib import Path

DATA_DIR = Path("challenges", "data")


def lines_to_lists(lines: list[str]) -> tuple[list[int], list[int]]:
    numbers = [line.split() for line in lines]
    left = [int(num) for num, _ in numbers]
    right = [int(num) for _, num in numbers]
    return left, right


def part_1(lines: list[str]) -> int:
    left, right = lines_to_lists(lines)

    return sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))


def part_2(lines: list[str]) -> int:
    left, right = lines_to_lists(lines)
    # Counter essentially creates a tally of values which appear in the `right`
    # list
    # i.e. [1, 1, 2, 3] becomes {1: 2, 2: 1, 3: 1}
    right_counts = Counter(right)

    return sum(num * right_counts[num] for num in left if num in right_counts)


if __name__ == "__main__":
    with open(DATA_DIR / "day_01.txt", "r") as f:
        input_lines = f.read().splitlines()
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
