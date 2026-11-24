#!/usr/bin/env python3
"""news-image-20261123 entry: copy the prepared front page to /output/entry.png.

Deterministic, no network, standard library only. The image itself was
composed in advance (see generate.py in the workspace, not submitted);
this program just delivers the exact same bytes on every run.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main():
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
