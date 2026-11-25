#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — one Wi-Fi network name.

Writes the winning name to /output/entry.txt (or $OUTPUT_DIR/entry.txt)
and prints exactly that one line to stdout.
"""

import os

ENTRY = "I Hacked Your Fridge, Dave"  # 26 chars; duel winner, 7-0 (see DUEL.md)


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Write exactly the name, no trailing newline: the gate counts every
    # character in entry.txt and the cap is 32.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
