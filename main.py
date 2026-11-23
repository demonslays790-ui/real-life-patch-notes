#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog.

Writes one deadpan patch note about a small real-life change to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only.
"""

import os
import sys

LINE = (
    "Patch 1.4: The washing machine now finishes when it says it will. "
    "Known issue: the extra 12 minutes were load-bearing."
)
# The joke rides on the register: a dry "Known issue" note that quietly
# reframes the machine's lying timer as a load-bearing feature of the
# household, not a bug. Keep the turn in the final words.


def main() -> int:
    # Gate: entry.txt must be a single line of UTF-8 text, 1 to 160
    # characters, not only whitespace. Refuse to write an invalid line.
    if not (1 <= len(LINE) <= 160) or not LINE.strip() or "\n" in LINE:
        print(
            f"error: line is {len(LINE)} characters; must be 1-160, one line",
            file=sys.stderr,
        )
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
