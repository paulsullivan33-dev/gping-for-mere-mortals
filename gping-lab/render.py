#!/usr/bin/env python3
"""Rebuild the final screen from a raw pseudo-terminal capture made by
pty-run.py, using the pyte terminal emulator. What comes out is the
screen as a person watching it at the end of the run would have seen
it (trailing blank lines removed).

Usage: render.py RAW_CAPTURE [COLUMNS ROWS]
"""
import sys

import pyte


def main() -> None:
    path = sys.argv[1]
    cols = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    rows = int(sys.argv[3]) if len(sys.argv) > 3 else 32
    screen = pyte.Screen(cols, rows)
    stream = pyte.ByteStream(screen)
    with open(path, "rb") as fh:
        stream.feed(fh.read())
    lines = [line.rstrip() for line in screen.display]
    while lines and not lines[-1]:
        lines.pop()
    print("\n".join(lines))


if __name__ == "__main__":
    main()
