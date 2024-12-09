from functools import wraps
from pathlib import Path
from time import perf_counter

DATA_DIR = Path("challenges", "data")
TEST_DATA_DIR = Path("tests", "data")


def todays_lines(file, split: bool = True, test: bool = False) -> str | list[str]:
    day = int(Path(file).stem.split("_")[-1])
    dir = TEST_DATA_DIR if test else DATA_DIR
    with open(dir / f"day_{day:02}.txt", "r") as f:
        data = f.read()
        if split:
            return data.splitlines()
        return data


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        s = perf_counter()
        result = func(*args, **kwargs)
        f = perf_counter()
        print(f"{func.__name__} ran in {f - s:.2f}s")
        return result

    return wrapper


if __name__ == "__main__":
    from time import sleep

    @timeit
    def something():
        sleep(2)
        return True

    something()
