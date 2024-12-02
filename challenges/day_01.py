from challenges.utils import DATA_DIR


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
    return sum(num * right.count(num) for num in left if num in right)


if __name__ == "__main__":
    with open(DATA_DIR / "day_01.txt", "r") as f:
        input_lines = f.read().splitlines()
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
