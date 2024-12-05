from challenges.utils import todays_lines


def count_xmas(lines: list[str]) -> int:
    total = 0
    for x, y in [
        (x, y)
        for y, row in enumerate(lines)
        for x, char in enumerate(row)
        if char == "X"
    ]:
        for x_offset, y_offset in [
            (x_offset, y_offset)
            for x_offset in range(-1, 2)
            for y_offset in range(-1, 2)
            if (x_offset, y_offset) != (0, 0)
        ]:
            for mult, letter in zip(range(1, 4), "MAS"):
                if (
                    len(lines) > (try_y := y + (y_offset * mult)) >= 0
                    and len(lines[0]) > (try_x := x + (x_offset * mult)) >= 0
                ):
                    if lines[try_y][try_x] != letter:
                        break
                    if letter == "S":
                        total += 1
    return total


def count_crosses(lines: list[str]) -> int:
    total = 0
    for x, y in [
        (x, y)
        for y, row in tuple(enumerate(lines))[1:-1]
        for x, char in tuple(enumerate(row))[1:-1]
        if char == "A"
    ]:
        if (
            {lines[y - 1][x - 1], lines[y + 1][x + 1]}
            == {lines[y + 1][x - 1], lines[y - 1][x + 1]}
            == {"M", "S"}
        ):
            total += 1
    return total


def part_1(lines: list[str]) -> int:
    return count_xmas(lines)


def part_2(lines: list[str]) -> int:
    return count_crosses(lines)


if __name__ == "__main__":
    input_lines = todays_lines(__file__)

    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
