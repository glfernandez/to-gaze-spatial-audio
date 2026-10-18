#!/usr/bin/env python3
"""Verify that every audio path referenced by the soundboard exists."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent
HTML = ROOT / "Rehearsal_Soundboard.html"
PATTERN = re.compile(r'''["'](SFX/[^"']+\.(?:wav|mp3|m4a|opus|flac))["']''', re.I)


def main() -> int:
    references = sorted(set(PATTERN.findall(HTML.read_text(encoding="utf-8"))))
    missing = [path for path in references if not (ROOT / path).is_file()]
    print(f"Referenced audio assets: {len(references)}")
    print(f"Missing audio assets: {len(missing)}")
    for path in missing:
        print(f"MISSING: {path}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
