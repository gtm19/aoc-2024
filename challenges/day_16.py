from heapq import heappop, heappush

from challenges.utils import make_grid, todays_lines


def part_1(grid: dict) -> int:
    grid = {k: v for k, v in grid.items() if v != "#"}
    prev = {}

    start = next(k for k in grid if grid[k] == "S")
    queue = [(0, i := 0, start, 1)]
    seen = set()

    while queue:
        distance, _, current, direction = heappop(queue)

        seen.add((current, direction))

        if grid[current] == "E":
            best = distance
            end = current
            break

        for d, score in zip(
            (1, 1j, -1j),
            (1, 1001, 1001),
        ):
            dist, i, nn, nd = (
                distance + score,
                i + 1,
                current + d * direction,
                d * direction,
            )
            if nn in grid and (nn, nd) not in seen:
                heappush(queue, (dist, i, nn, nd))
                prev[nn] = prev.get(nn, set()) | {current}

    return best


def part_2(grid: dict) -> int:
    pass


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=True)
    grid = make_grid(input_lines)
    print("\n")
    print("PART 1: ", part_1(grid))
    print("PART 2: ", part_2(grid))
