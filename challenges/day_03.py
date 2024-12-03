import re

from challenges.utils import todays_lines


def extract_mults(lines: str) -> tuple[tuple[int, int], ...]:
    regex = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = regex.findall(lines)
    return tuple(map(lambda x: (int(x[0]), int(x[1])), matches))


def filter_dos(lines: str) -> str:
    regex = re.compile(r"(?:^|do\(\)).*?(?:$|don't\(\))")
    matches = regex.findall(lines)
    return "".join(matches)


def part_1(lines: str) -> int:
    return sum(x * y for x, y in extract_mults(lines))


def part_2(lines: str) -> int:
    filtered = filter_dos(lines)
    return sum(x * y for x, y in extract_mults(filtered))


if __name__ == "__main__":
    input_lines = "".join(todays_lines(__file__, split=False).splitlines())

    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
