from collections import Counter

from challenges.utils import todays_lines


def blink(stones: dict[int, int], times: int = 1) -> None:
    for _ in range(times):
        for marked_with, count in list(stones.items()):
            stones[marked_with] -= count
            if len(str(marked_with)) % 2 == 0:
                stones[int(str(marked_with)[: len(str(marked_with)) // 2])] += count
                stones[int(str(marked_with)[len(str(marked_with)) // 2 :])] += count
            elif marked_with == 0:
                stones[1] += count
            else:
                stones[marked_with * 2024] += count


def part_1(lines: list[str]) -> int:
    stones = Counter(list(map(int, lines[0].split())))
    blink(stones, times=25)
    return sum(stones.values())


def part_2(lines: list[str]) -> int:
    stones = Counter(list(map(int, lines[0].split())))
    blink(stones, times=75)
    return sum(stones.values())


if __name__ == "__main__":
    input_lines = todays_lines(__file__)
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
