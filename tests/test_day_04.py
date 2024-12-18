import pytest

from challenges.day_04 import part_1, part_2

from .utils import TEST_DATA_DIR

with open(TEST_DATA_DIR / "day_04.txt", "r") as f:
    lines = f.read().splitlines()


def test_part_1():
    assert part_1(lines) == 18


def test_part_2():
    assert part_2(lines) == 9
