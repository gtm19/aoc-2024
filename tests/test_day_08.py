from challenges.day_08 import part_1, part_2
from challenges.utils import todays_lines

lines = todays_lines(__file__, test=True)


def test_part_1():
    assert part_1(lines) == 14


def test_part_2():
    assert part_2(lines) == 34
