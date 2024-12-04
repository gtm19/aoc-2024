from itertools import product

from challenges.utils import todays_lines


def count_xmas(lines: list[str]) -> int:
    total = 0
    for x, y in product(range(len(lines)), range(len(lines[0]))):
        if lines[y][x] == "X":
            for x_offset, y_offset in [
                (1, 0),
                (0, 1),
                (1, 1),
                (-1, 0),
                (0, -1),
                (-1, -1),
                (1, -1),
                (-1, 1),
            ]:
                try:
                    if (
                        "".join(
                            lines[try_y][try_x]
                            for mult in (1, 2, 3)
                            if len(lines) > (try_y := y + (y_offset * mult)) >= 0
                            and len(lines[0]) > (try_x := x + (x_offset * mult)) >= 0
                        )
                        == "MAS"
                    ):
                        total += 1
                except IndexError:
                    continue
    return total


def count_crosses(lines: list[str]) -> int:
    total = 0
    for x, y in product(range(1, len(lines) - 1), range(1, len(lines[0]) - 1)):
        if lines[y][x] == "A":
            try:
                if (
                    {lines[y - 1][x - 1], lines[y + 1][x + 1]}
                    == {lines[y + 1][x - 1], lines[y - 1][x + 1]}
                    == {"M", "S"}
                ):
                    total += 1
            except IndexError:
                continue
    return total


def part_1(lines: list[str]) -> int:
    return count_xmas(lines)


def part_2(lines: list[str]) -> int:
    return count_crosses(lines)


if __name__ == "__main__":
    input_lines = todays_lines(__file__)

    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
