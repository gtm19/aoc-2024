from itertools import cycle
from time import perf_counter

from challenges.utils import todays_lines

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))

OBSTACLE = "#"
START = DIRECTIONS[0]

# TODO: take another look at this where the obstacles are a list of locations
# which you append to for part 2 - should be much quicker


def make_grid(lines: list[str]) -> dict[tuple[int, int] : str]:
    return {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}


def walk_around(grid, start) -> tuple[list, bool]:
    direction_cycle = cycle(DIRECTIONS)

    direction = next(direction_cycle)
    x, y = start
    visited = [(direction, (x, y))]
    while True:
        next_x, next_y = x + direction[0], y + direction[1]
        next_value = grid.get((next_x, next_y))
        if not next_value:
            infinite = False
            break
        if (direction, (next_x, next_y)) in visited:
            infinite = True
            break
        if next_value == "#":
            direction = next(direction_cycle)
        else:
            visited.append((direction, (next_x, next_y)))
            x, y = next_x, next_y
    return visited, infinite


def part_1(grid, start) -> int:
    visited = walk_around(grid, start)[0]
    return len({loc[1] for loc in visited})


def part_2(grid, start) -> int:
    visited = walk_around(grid, start)[0]
    return sum(
        walk_around(grid | {obs: "#"}, start)[1]
        for obs in {loc[1] for loc in visited}
        if obs != start
    )


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)

    grid = make_grid(input_lines)
    start = [k for k, v in grid.items() if v == "^"][0]

    print("PART 1: ", part_1(grid, start))
    print("PART 2: ", part_2(grid, start))
