#!/usr/bin/env python3
"""Write one funny single-line developer excuse to /output/entry.txt.

Pure stdlib, deterministic: the same bytes on every run.
"""

from pathlib import Path

LINE = (
    "My change didn't break production \u2014 it was the first thing to actually "
    "run that code path in three years, and the bug was already waiting."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert "\n" not in LINE, "line must be a single line"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
