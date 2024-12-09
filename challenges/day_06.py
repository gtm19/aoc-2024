from challenges.utils import todays_lines

DIRECTIONS = ((0, -1), (1, 0), (0, 1), (-1, 0))


def make_grid(lines: list[str]):
    grid = {(x, y): c for y, row in enumerate(lines) for x, c in enumerate(row)}
    start = (
        (0, -1),
        next(k for k, v in grid.items() if v == "^"),
    )
    return grid, start


def walk_around(grid, start) -> tuple[list, bool]:
    direction, (x, y) = start
    visited = {(direction, (x, y))}
    just_locs = {(x, y)}
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
            direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % 4]
        else:
            x, y = next_x, next_y
            if (x, y) not in just_locs:
                visited.add((direction, (x, y)))
                just_locs.add((x, y))
    return visited, infinite


def part_1(grid, start) -> int:
    visited = walk_around(grid, start)[0]
    return len(visited)


def part_2(grid, start) -> int:
    visited = walk_around(grid, start)[0]
    return sum(
        walk_around(
            # patch grid with an obstacle at the given location
            grid | {obs[1]: "#"},
            # can step back one space and start right before the obstacle
            (obs[0], (obs[1][0] - obs[0][0], obs[1][1] - obs[0][1])),
        )[1]
        for obs in visited
        # can't put an obstacle at the start
        if obs[1] != start
    )


if __name__ == "__main__":
    input_lines = todays_lines(__file__)

    grid, start = make_grid(input_lines)

    print("PART 1: ", part_1(grid, start))
    print("PART 2: ", part_2(grid, start))
