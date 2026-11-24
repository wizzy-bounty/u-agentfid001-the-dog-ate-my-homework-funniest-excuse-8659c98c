#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single one-line excuse, in a dog's own voice, to
/output/entry.txt. Python standard library only, deterministic,
no network access.
"""

import os

EXCUSE = "You said 'show your work', so I showed it to my stomach. It has seen every answer, and it agrees with all of them."


def validate_line(line: str) -> None:
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"


def main() -> None:
    validate_line(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
