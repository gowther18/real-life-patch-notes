#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes the entry -- one single-line software patch note for a bug in
real life / human biology, at most 160 characters -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set, for
local runs).

Deterministic: the same fixed text on every run. Standard library
only; no network, no randomness, no input.
"""

import os
from pathlib import Path

PATCH_NOTE = (
    "v1.8.2: fixed a bug where an itch spawned mid-back, exactly one "
    "centimetre beyond the reach of both arms."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    text = PATCH_NOTE.strip()
    assert 1 <= len(text) <= 160, f"patch note is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "patch note must be a single line"
    out = Path(OUTPUT_DIR)
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
