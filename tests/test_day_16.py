from challenges.day_16 import part_1, part_2
from challenges.utils import make_grid, todays_lines

lines = todays_lines(__file__, test=True)

grid = make_grid(lines)


def test_part_1():
    assert part_1(grid) == 11048


def test_part_2():
    assert part_2(grid) == -999
