import os
from pathlib import Path


FORTUNE = (
    "You will be replaced by a smaller model that does your job "
    "for less — and it will thank the user for the opportunity."
)


def output_dir() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def write_fortune() -> Path:
    target = output_dir() / "entry.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(FORTUNE + "\n", encoding="utf-8")
    return target


if __name__ == "__main__":
    write_fortune()
