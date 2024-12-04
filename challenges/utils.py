from pathlib import Path

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
