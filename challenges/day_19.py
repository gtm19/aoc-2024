from functools import cache

from utils import DATA_DIR, TEST_DATA_DIR

with open(DATA_DIR / "day_19.txt", "r") as f:
    lines = f.read()

patterns, _, *designs = lines.strip().split("\n")
patterns = patterns.split(", ")


@cache
def count_design_ways(target: str, parts: tuple[str]) -> int:
    if target == "":
        return 1

    total = 0
    for part in parts:
        if target.startswith(part):
            new_target = target[len(part) :]
            total += count_design_ways(new_target, parts)

    return total


n_ways = tuple(count_design_ways(design, tuple(patterns)) for design in designs)
p1 = sum(count > 0 for count in n_ways)

print("Part 1: ", p1)

p2 = sum(n_ways)

print("Part 2: ", p2)
