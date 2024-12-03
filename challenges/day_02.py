from challenges.utils import todays_lines


def check_safety(nums: list[int]) -> bool:
    diffs = [x_2 - x_1 for x_1, x_2 in zip(nums[:-1], nums[1:])]
    safe = (set(diffs) <= {-3, -2, -1}) or (set(diffs) <= {1, 2, 3})
    return safe


def part_1(lines: list[list[int]]) -> int:
    return sum(check_safety(line) for line in lines)


def part_2(lines: list[list[int]]) -> int:
    return sum(
        check_safety(line)
        or (any(check_safety(line[:i] + line[i + 1 :]) for i in range(len(line))))
        for line in lines
    )


if __name__ == "__main__":
    input_lines = [list(map(int, line.split())) for line in todays_lines(__file__)]
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
