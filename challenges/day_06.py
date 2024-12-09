from challenges.utils import todays_lines


def make_grid(lines: list[str]):
    # used complex numbers, inspired by
    # https://www.reddit.com/r/adventofcode/comments/1h7tovg/comment/m0o44m5/
    grid = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    start = (
        -1j,
        next(k for k, v in grid.items() if v == "^"),
    )
    return grid, start


def walk_around(grid, start) -> tuple[list, bool]:
    direction, location = start
    visited = set()
    just_locs = set()
    while location in grid and (direction, location) not in visited:
        if location not in just_locs:
            visited.add((direction, location))
        just_locs.add(location)
        if grid.get(location + direction) == "#":
            # rotate
            direction *= 1j
        else:
            # move
            location += direction
    return visited, (direction, location) in visited


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
            (obs[0], obs[1] - obs[0]),
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
