"""One Line, One Laugh -- entry program.

Writes one funny line (at most 140 characters) to OUTPUT_DIR/entry.txt.
Standard library only, no network, same bytes every run.
"""

import os

ENTRY = "My therapist told me to stop overthinking, so I built a spreadsheet to track it. It has 14 tabs and a mood ring."

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    # Gate: 1 to 140 characters of UTF-8, not only white space.
    assert ENTRY.strip() and 1 <= len(ENTRY) <= 140
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
