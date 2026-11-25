"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes the GPS's one-line excuse to /output/entry.txt.
Stdlib only.
"""

import os

TEXT = "It was a shortcut. The map said turn left at the lake, it just never said the lake was the road."


def main():
    # Self-gate mirroring the sealed scorer: 1-200 chars, non-whitespace, one line.
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT.strip(), "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"chars: {len(TEXT)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
