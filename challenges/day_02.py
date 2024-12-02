from challenges.utils import DATA_DIR


def check_safety(line: str, tolerant: bool = False) -> bool:
    nums = [int(num) for num in line.split()]
    diffs = [x_2 - x_1 for x_1, x_2 in zip(nums[:-1], nums[1:])]
    safe = all(-3 <= diff <= -1 for diff in diffs) or all(
        1 <= diff <= 3 for diff in diffs
    )
    if tolerant and not safe:
        for i in range(len(nums)):
            filtered_nums = [num for j, num in enumerate(nums) if i != j]
            filtered_diffs = [
                x_2 - x_1 for x_1, x_2 in zip(filtered_nums[:-1], filtered_nums[1:])
            ]
            safe = all(-3 <= diff <= -1 for diff in filtered_diffs) or all(
                1 <= diff <= 3 for diff in filtered_diffs
            )
            if safe:
                break
    return safe


def part_1(lines: list[str]) -> int:
    return sum(check_safety(line) for line in lines)


def part_2(lines: list[str]) -> int:
    return sum(check_safety(line, tolerant=True) for line in lines)


if __name__ == "__main__":
    with open(DATA_DIR / "day_02.txt", "r") as f:
        input_lines = f.read().splitlines()
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
