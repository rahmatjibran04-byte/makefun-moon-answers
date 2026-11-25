#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes a single line, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it.
No network, no arguments, no side effects beyond /output/entry.txt.
"""

import os

ENTRY = (
    "Four billion years of wishes, howls, and 3 a.m. promises \u2014 "
    "and not one of you ever asked how I'm doing."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 240, "entry must be 1-240 characters"
    assert text == text.strip() and "\n" not in text, "entry must be one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    os.chmod("/output/entry.txt", 0o644)
    # Read-back: prove the file on disk is exactly the gated line.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "read-back mismatch"
    assert 1 <= len(written.rstrip("\n")) <= 240, "gate re-check failed"


if __name__ == "__main__":
    main()
