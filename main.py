"""Globe Menetas entry program (Python 3.13, standard library only).

The program ships the finished picture as entry.jpg next to this file and
simply hands those exact bytes to the grader: it reads entry.jpg and writes
the identical bytes to entry.png inside the output directory. No network,
no randomness, no clock reads, so every run produces the same file.

The output directory comes from MAKEFUN_OUTPUT_DIR; when that variable is
not set the grader's /output directory is used. Outside the grader you can
point it anywhere, for example:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
"""

import os
from pathlib import Path

ENTRY_FILENAME = "entry.jpg"
OUTPUT_FILENAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir() -> Path:
    chosen = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    target = Path(chosen)
    target.mkdir(parents=True, exist_ok=True)
    return target


def copy_entry() -> tuple[int, Path, Path]:
    here = Path(__file__).resolve().parent
    source = here / ENTRY_FILENAME
    if not source.is_file():
        raise FileNotFoundError(f"entry image missing: {source}")
    payload = source.read_bytes()
    destination = resolve_output_dir() / OUTPUT_FILENAME
    destination.write_bytes(payload)
    written = destination.stat().st_size
    if written != len(payload):
        raise OSError(f"short write: {destination} got {written} of {len(payload)} bytes")
    return len(payload), source, destination


def run() -> None:
    size, source, destination = copy_entry()
    print(f"wrote {size} bytes: {source.name} -> {destination}")


if __name__ == "__main__":
    run()
