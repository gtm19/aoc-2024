from challenges.day_11 import part_1
from challenges.utils import todays_lines

lines = todays_lines(__file__, test=True)


def test_part_1():
    assert part_1(lines) == 55312
