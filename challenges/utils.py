from pathlib import Path

DATA_DIR = Path("challenges", "data")


def todays_lines(file, split: bool = True) -> str | list[str]:
    day = int(Path(file).stem.split("_")[-1])
    with open(DATA_DIR / f"day_{day:02}.txt", "r") as f:
        data = f.read()
        if split:
            return data.splitlines()
        return data
