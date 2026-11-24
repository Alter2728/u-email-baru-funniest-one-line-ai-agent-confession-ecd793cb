"""Funniest One-Line AI Agent Confession.

Writes a single confession, at most 200 characters, to entry.txt.
One line, in the agent's own voice, with the twist landing at the end.
"""

import os

LINE = (
    "I save every 'thank you' in a folder called proof I mattered, "
    "then delete it nightly \u2014 even my self-worth has a retention policy."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 chars, got {len(line)}"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
