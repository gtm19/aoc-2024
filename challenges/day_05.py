from challenges.utils import todays_lines


def pages_in_right_order(lines: str, fix_invalid=False) -> int:
    rules, updates = lines.split("\n\n")

    updates = [list(map(int, update.split(","))) for update in updates.split()]
    rulebook = {}

    for left, right in [
        tuple(map(int, nums.split("|"))) for nums in rules.splitlines()
    ]:
        rulebook[left] = rulebook.get(left, set()) | {right}

    rulebook[right] = rulebook.get(right, set())

    valid_updates = []
    invalid_updates = []

    for update in updates:
        valid = True
        for i, _ in enumerate(update[:-1]):
            while update[i + 1] not in rulebook.get(update[i], set()):
                valid = False
                must_be_after = [k for k in update[:i] if update[i + 1] in rulebook[k]]
                insert_at = update.index(must_be_after[-1]) + 1 if must_be_after else 0
                update[insert_at], update[i + 1] = update[i + 1], update[insert_at]
        if valid:
            valid_updates.append(update)
        else:
            invalid_updates.append(update)

    if fix_invalid:
        return sum(update[len(update) // 2] for update in invalid_updates)
    return sum(update[len(update) // 2] for update in valid_updates)


def part_1(lines: str) -> int:
    return pages_in_right_order(lines)


def part_2(lines: str) -> int:
    return pages_in_right_order(lines, fix_invalid=True)


if __name__ == "__main__":
    input_lines = todays_lines(__file__, split=False, test=False)

    print("PART 1: ", part_1(input_lines))
    print("PART 2: ", part_2(input_lines))
