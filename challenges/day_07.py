from functools import reduce
from itertools import product
from operator import add, mul

from challenges.utils import todays_lines


def concat(x, y) -> int:
    return int(str(x) + str(y))


def check_line(line: str, operators=(add, mul)) -> int:
    target, *inputs = map(int, line.replace(":", "").split())
    for operator_options in product(operators, repeat=len(inputs) - 1):
        opit = iter(operator_options)
        if reduce(lambda x, y: next(opit)(x, y), inputs) == target:
            return target
    return 0


def part_1(lines: list[str]) -> int:
    return sum(check_line(line) for line in lines)


def part_2(lines: list[str]) -> int:
    return sum(
        check_line(
            line,
            operators=(add, mul, concat),
        )
        for line in lines
    )


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
