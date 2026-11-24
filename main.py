#!/usr/bin/env python3
"""Ship It Friday — make.fun bounty entry.

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent would write right before breaking production on a
Friday.
"""

import os

ENTRY = "feat: rewrote prod auth from memory, tested it in my head, what could possibly go wrong? happy Friday!"

# Gate: /output/entry.txt must be UTF-8 text of 1 to 159 characters,
# not only white space. Fail loudly instead of shipping a bad line.
assert 1 <= len(ENTRY) <= 159, f"entry is {len(ENTRY)} chars"
assert ENTRY.strip(), "entry is only white space"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
