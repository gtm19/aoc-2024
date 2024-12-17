from functools import cache
from heapq import heappop, heappush

from challenges.utils import make_grid, todays_lines


@cache
def trace_path(input_lines: str) -> tuple[int, int]:
    grid = make_grid(input_lines.splitlines())
    grid = {k: v for k, v in grid.items() if v != "#"}
    dist = {}

    start = next(k for k in grid if grid[k] == "S")
    end = next(k for k in grid if grid[k] == "E")
    queue = [(0, i := 0, start, 1, {start})]

    best = float("inf")

    good_squares = set()

    while queue:
        distance, _, current, direction, previous = heappop(queue)

        if distance > dist.get((current, direction), float("inf")):
            continue
        dist[current, direction] = distance

        if current == end and distance <= best:
            best = distance
            good_squares |= previous

        for d, score in zip((1, 1j, -1j), (1, 1001, 1001)):
            ndist, i, nn, nd = (
                distance + score,
                i + 1,
                current + d * direction,
                d * direction,
            )
            if nn in grid:
                heappush(queue, (ndist, i, nn, nd, previous | {nn}))

    return best, len(good_squares)


def part_1(input_lines: str) -> int:
    best, _ = trace_path(input_lines)

    return best


def part_2(input_lines: str) -> int:
    _, n_good_squares = trace_path(input_lines)

    return n_good_squares


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False, split=False)
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
