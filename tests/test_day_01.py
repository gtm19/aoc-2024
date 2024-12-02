from challenges.day_01 import part_1, part_2

with open("tests/data/day_01.txt", "r") as f:
    lines = f.read().splitlines()


def test_part_1():
    assert part_1(lines) == 11


def test_part_2():
    assert part_2(lines) == 31
