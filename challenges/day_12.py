from challenges.utils import todays_lines


def make_grid(lines: list[str]) -> dict:
    return {x + y * 1j: c for y, row in enumerate(lines) for x, c in enumerate(row)}


def get_price(grid: dict, use_sides: bool = False) -> list[set]:
    unvisited = set(grid.keys())

    price = 0

    while unvisited:
        area = 0
        perimeter = 0
        sides = 0
        queue = set([unvisited.pop()])

        while queue:
            current = queue.pop()
            unvisited.discard(current)
            area += 1
            direction = -1j
            for _ in range(4):
                new = current + direction
                if new in grid and grid[new] == grid[current]:
                    if new in unvisited:
                        queue.add(new)
                else:
                    perimeter += 1
                    next_new = current + (direction * 1j)
                    if not (
                        next_new in grid
                        and grid[next_new] == grid[current]
                        and grid.get(next_new + direction) != grid[current]
                    ):
                        sides += 1

                direction *= 1j
        price += area * (sides if use_sides else perimeter)

    return price


def part_1(grid: dict) -> int:
    return get_price(grid)


def part_2(grid: dict) -> int:
    return get_price(grid, use_sides=True)


if __name__ == "__main__":
    input_lines = todays_lines(__file__, test=False)
    grid = make_grid(input_lines)
    print("PART 1: ", part_1(grid))
    print("PART 2: ", part_2(grid))
