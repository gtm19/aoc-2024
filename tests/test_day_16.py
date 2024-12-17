from challenges.day_16 import part_1, part_2
from challenges.utils import todays_lines

lines = todays_lines(__file__, test=True, split=False)


def test_part_1():
    assert part_1(lines) == 11048


def test_part_2():
    assert part_2(lines) == 64
