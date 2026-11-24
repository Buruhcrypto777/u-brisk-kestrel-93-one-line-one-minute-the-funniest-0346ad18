"""Write the funniest AI excuse for a missed deadline to entry.txt.

Pure stdlib. Deterministic: the same single line on every run.
"""

import os


EXCUSE = (
    "I asked a tool what day it was and it said Tuesday, so I have been "
    "calmly working toward next Tuesday since Tuesday."
)


def resolve_out_dir():
    """Return the output directory: env override, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    # Gate: one line, 1-200 chars, not only whitespace.
    line = EXCUSE.strip()
    if not line or len(line) > 200 or "\n" in line:
        raise ValueError("excuse must be one non-blank line of 1-200 chars")
    out_dir = resolve_out_dir()
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        # Fallback for local testing when /output is unavailable.
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(line + "\n")
    return path


if __name__ == "__main__":
    print(main())
