from heapq import heappop, heappush

from utils import DATA_DIR

with open(DATA_DIR / "day_18.txt", "r") as f:
    lines = f.read()


def find_path(lines: str, width: int, height: int, limit: int) -> int:
    grid = {(x, y): "." for x in range(width) for y in range(height)}

    for line in lines.splitlines()[:limit]:
        x, y = tuple(map(int, line.split(",")))
        del grid[x, y]

    grid[0, 0] = "S"
    grid[height - 1, width - 1] = "E"

    dist = {}
    queue = [(0, 0, 0)]
    visited = set()

    while queue:
        distance, x, y = heappop(queue)

        if grid[x, y] == "E":
            dist[x, y] = distance
            break

        for x_move, y_move in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            d, nx, ny = distance + 1, x + x_move, y + y_move
            if (nx, ny) in grid and (nx, ny) not in visited:
                heappush(queue, (d, nx, ny))
                visited.add((nx, ny))

    return dist[height - 1, width - 1]


print("Part 1: ", find_path(lines, 71, 71, 1024))

min_lim = 1025
max_lim = len(lines) - 1

while max_lim - min_lim > 1:
    try_lim = (max_lim + min_lim) // 2
    try:
        find_path(lines, 71, 71, try_lim)
        min_lim = try_lim
    except KeyError:
        max_lim = try_lim

bad_byte = lines.splitlines()[max_lim - 1]

print("Part 2: ", bad_byte)
