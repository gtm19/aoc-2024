from challenges.day_06 import make_grid, part_1, part_2

from .utils import TEST_DATA_DIR

with open(TEST_DATA_DIR / "day_06.txt", "r") as f:
    lines = f.read().splitlines()
    grid, start = make_grid(lines)


def test_part_1():
    assert part_1(grid, start) == 41


def test_part_2():
    assert part_2(grid, start) == 6
