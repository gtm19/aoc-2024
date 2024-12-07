import re
from itertools import cycle

from challenges.utils import todays_lines

DIRECTIONS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}

DIRECTION_CYCLER = cycle(DIRECTIONS.keys())

OBSTACLE = "#"
START = next(DIRECTION_CYCLER)


def inside_grid(loc, grid: list[str]) -> bool:
    x, y = loc
    if x < 0 or y < 0 or x > len(grid[0]) - 1 or y > len(grid) - 1:
        return False
    return True


def part_1(lines: list[str]) -> int:
    visited = [
        (START, (line.find(START), i)) for i, line in enumerate(lines) if START in line
    ]
    direction, (x, y) = visited[-1]
    while True:
        next_x, next_y = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
        if not inside_grid((next_x, next_y), lines):
            break
        next_value = lines[next_y][next_x]
        if next_value == "#":
            direction = next(DIRECTION_CYCLER)
            continue
        else:
            visited.append((direction, (next_x, next_y)))
            x, y = next_x, next_y
            continue
    return len(set([loc[1] for loc in visited]))


def part_2(lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)

    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
