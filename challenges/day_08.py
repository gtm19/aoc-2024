from itertools import permutations

from challenges.utils import todays_lines


def part_1(lines: list[str]) -> int:
    grid = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    frequencies = set(grid.values()) - {"."}
    antinode_locations = set()
    for freq in frequencies:
        locs = set(k for k, v in grid.items() if v == freq)
        for loc_from, loc_to in permutations(locs, 2):
            antinode = 2 * loc_to - loc_from
            if antinode in grid:
                antinode_locations.add(antinode)
    return len(antinode_locations)


def part_2(lines: list[str]) -> int:
    grid = {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}
    frequencies = set(grid.values()) - {"."}
    antinode_locations = set()
    for freq in frequencies:
        locs = set(k for k, v in grid.items() if v == freq)
        for loc_from, loc_to in permutations(locs, 2):
            mult, direction = 0, loc_to - loc_from
            while (antinode := (loc_to + mult * direction)) in grid:
                antinode_locations.add(antinode)
                mult += 1
    return len(antinode_locations)


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)
    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
