from pathlib import Path


def datafile(name: str) -> str:
    return Path(__file__).parents[1] / "data" / name

def readfile(name: str) -> str:
    with open(name, "rt", encoding="utf-8") as f:
        return f.read().strip()
