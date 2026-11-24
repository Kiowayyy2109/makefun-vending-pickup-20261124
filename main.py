#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single one-line pickup line (at most 200 characters), spoken by
a vending machine to a passing human, to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt).

Python 3 standard library only. No network. Deterministic: the same line
is written on every run.
"""

import os
import sys

# The selected line: the machine charges exact change to everyone else,
# but the price for you is one smile -- and it gives no change on those.
# The "change" wordplay is the machine's own world doing the comic work,
# and the punch lands in the last few words.
ENTRY = (
    "I charge exact change for everyone else. For you, the price is one "
    "smile \u2014 and I don't give change on those."
)

MAX_CHARS = 200


def main() -> int:
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(ENTRY), MAX_CHARS)
        )
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")

    out_target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output/entry.txt"
    out_path = (
        out_target
        if out_target.endswith(".txt")
        else os.path.join(out_target, "entry.txt")
    )
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")

    # Verify the gate on what was actually written: 1-200 characters,
    # not only whitespace, and byte-identical to the selected line.
    with open(out_path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY + "\n":
        raise ValueError("written entry does not match the selected line")
    if written.count("\n") != 1 or not written.endswith("\n"):
        raise ValueError("written entry is not exactly one line")
    if not 1 <= len(written.rstrip("\n")) <= MAX_CHARS:
        raise ValueError("written entry fails the 1-200 character gate")
    return 0


if __name__ == "__main__":
    sys.exit(main())
