import re
from itertools import cycle

from challenges.utils import todays_lines

DIRECTIONS = {
    "^": (0, -1),
    ">": (1, 0),
    "v": (0, 1),
    "<": (-1, 0),
}


OBSTACLE = "#"
START = "^"


def inside_grid(loc, grid: list[str]) -> bool:
    x, y = loc
    if x < 0 or y < 0 or x > len(grid[0]) - 1 or y > len(grid) - 1:
        return False
    return True


def walk_around(lines: list[str]) -> tuple[list, bool]:
    DIRECTION_CYCLER = cycle(DIRECTIONS.keys())
    visited = [
        (START, (line.find(START), i)) for i, line in enumerate(lines) if START in line
    ]
    direction, (x, y) = visited[-1]
    while True:
        next_x, next_y = x + DIRECTIONS[direction][0], y + DIRECTIONS[direction][1]
        if not inside_grid((next_x, next_y), lines):
            infinite = False
            break
        if (direction, (next_x, next_y)) in visited:
            infinite = True
            break
        next_value = lines[next_y][next_x]
        if next_value == OBSTACLE:
            direction = next(DIRECTION_CYCLER)
        else:
            visited.append((direction, (next_x, next_y)))
            x, y = next_x, next_y
    return visited, infinite


def part_1(lines: list[str]) -> int:
    visited = walk_around(lines)[0]
    return len({loc[1] for loc in visited})


def part_2(lines: list[str]) -> int:
    visited = walk_around(lines)[0]
    infinites = 0
    checked = 0
    for x, y in {loc[1] for loc in visited}:
        checked += 1
        if lines[y][x] == START:
            continue
        lines[y] = lines[y][:x] + OBSTACLE + lines[y][x + 1 :]
        infinites += int(walk_around(lines)[1])
        lines[y] = lines[y][:x] + "." + lines[y][x + 1 :]
    return infinites


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
