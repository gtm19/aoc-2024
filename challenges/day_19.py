from functools import cache

from utils import DATA_DIR

with open(DATA_DIR / "day_19.txt", "r") as f:
    lines = f.read()

PATTERNS, _, *designs = lines.strip().split("\n")


@cache
def count_design_ways(target: str) -> int:
    return int(target == "") or sum(
        count_design_ways(target.removeprefix(part))
        for part in PATTERNS.split(", ")
        if target.startswith(part)
    )


n_ways = tuple(count_design_ways(design) for design in designs)

print("Part 1: ", sum(map(bool, n_ways)))

print("Part 2: ", sum(n_ways))
