from itertools import combinations

from utils import DATA_DIR, TEST_DATA_DIR

with open(DATA_DIR / "day_20.txt", "r") as f:
    grid = {
        x + y * 1j: c
        for y, line in enumerate(f.read().splitlines())
        for x, c in enumerate(line)
        if c != "#"
    }

(start,) = (k for k, v in grid.items() if v == "S")

path = [start]

while True:
    pos = path[-1]

    if grid[pos] == "E":
        break

    for d in (1, -1j, -1, 1j):
        next_pos = pos + d
        if next_pos in grid and next_pos not in path:
            path.append(next_pos)
            break

p1 = 0
p2 = 0
for (i, start), (j, end) in combinations(enumerate(path), 2):
    steps = abs((start - end).real) + abs((start - end).imag)
    if 2 <= steps <= 20 and j - i - steps >= 100:
        p2 += 1
        if steps == 2:
            p1 += 1

print("Part 1: ", p1)
print("Part 2: ", p2)
