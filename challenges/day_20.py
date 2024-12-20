from utils import DATA_DIR, TEST_DATA_DIR

with open(DATA_DIR / "day_20.txt", "r") as f:
    grid = {
        x + y * 1j: c
        for y, line in enumerate(f.read().splitlines())
        for x, c in enumerate(line)
    }

(start,) = (k for k, v in grid.items() if v == "S")

path = [start]
cheats = 0
end_found = False

while not end_found:
    pos = path[-1]

    if grid[pos] == "E":
        end_found = True

    for d in (1, -1j, -1, 1j):
        next_pos = pos + d
        if next_pos in grid:
            if grid[next_pos] == "#":
                if next_pos + d in grid and grid[next_pos + d] != "#":
                    if next_pos + d in path:
                        cheat_length = (
                            abs(path.index(pos) - path.index(next_pos + d)) - 2
                        )
                        if cheat_length >= 100:
                            cheats += 1
            elif next_pos not in path:
                path.append(next_pos)

print("Part 1: ", cheats)
