#!/usr/bin/env python3
"""Publish the one-letter entry for the make.fun bounty
"One Letter for Your Day".

The letter is ``Z``. Behind it sits the word that describes the day:
zero sleep — a zombie day. It is the most vivid of the letters whose
hidden word lands at once: a sharp, specific picture (a day run on no
sleep), funny in the way everyone recognises, and honest rather than
performed. The judge reads the single letter and the word behind it;
``Z`` carries that word harder than any vaguer mood letter.

The letter lives in ``entry.txt`` next to this file. This program
reads it, checks it against the bounty gate (UTF-8 text, exactly one
character, a letter from A to Z), writes that exact character to
``entry.txt`` in the output directory, and reads it back to confirm
the published bytes match. Standard library only: no network access,
no clock reads, no randomness, so two runs always produce identical
output.

The output directory is ``$MAKEFUN_OUTPUT_DIR`` when set, else
``/output``. Pass ``--output-dir <dir>`` to choose it on the command
line instead, or ``--verify-only`` to check the letter without
writing anything.
"""

import argparse
import os
import sys
from pathlib import Path


def load_letter() -> str:
    here = Path(__file__).resolve().parent
    text = (here / "entry.txt").read_text(encoding="utf-8")
    return text.strip()


def validate(text: str) -> None:
    if len(text) != 1:
        raise SystemExit(
            f"entry is {len(text)} characters, must be exactly one"
        )
    if not ("A" <= text <= "Z"):
        raise SystemExit("entry must be a single letter from A to Z")


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default=None,
                        help="directory to write entry.txt into")
    parser.add_argument("--verify-only", action="store_true",
                        help="validate the letter without writing anything")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    args = parse_args(argv)
    text = load_letter()
    validate(text)
    if args.verify_only:
        print(f"Valid: {text!r}")
        return 0
    out_dir = Path(args.output_dir or os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    published = out_path.read_text(encoding="utf-8")
    if published != text:
        raise SystemExit("published entry does not match entry.txt")
    print(f"Wrote {text!r} to {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
