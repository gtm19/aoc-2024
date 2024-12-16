from challenges.utils import make_grid, todays_lines


def part_1(grid: dict) -> int:
    grid = {k: v for k, v in grid.items() if v != "#"}
    # dist = {(k, d): float("inf") for k in grid for d in (1, 1j, -1j, -1)}
    dist = {}
    prev = {}
    to_visit = set((k, d) for k in grid.keys() for d in (1, 1j, -1j, -1))

    start = next(k for k in grid if grid[k] == "S")
    finish = next(k for k in grid if grid[k] == "E")
    dist[(start, 1)] = 0

    while to_visit:
        current, direction = sorted(
            list(set(dist) & to_visit), key=lambda v: dist.get(v, float("inf"))
        )[0]

        if current == finish:
            break

        to_visit.remove((current, direction))
        # next moves:
        #  - forward in current direction (1 point) [(current + dir, dir)]
        #  - rotate left (1000 points) [(current, dir * 1j)]
        #  - rotate right (1000 points) [current, dir * -1j]
        for next_node, next_dir, distance in zip(
            (current + direction, current, current),
            (direction, direction * 1j, direction * -1j),
            (1, 1000, 1000),
        ):
            if next_node in grid:
                new_dist = dist[(current, direction)] + distance
                if new_dist <= dist.get((next_node, next_dir), float("inf")):
                    dist[(next_node, next_dir)] = new_dist
                    if distance == 1:
                        prev[next_node] = prev.get(next_node, set()) | {current}

    return int(min(v for (node, _), v in dist.items() if node == finish))


def part_2(grid: dict) -> int:
    pass


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=True)
    grid = make_grid(input_lines)
    print("\n")
    print("PART 1: ", part_1(grid))
    print("PART 2: ", part_2(grid))
