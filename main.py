"""Two Robots in an Elevator - entry program.

Writes one line of awkward small talk between two robots sharing
an elevator ride to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Standard library only; deterministic: the same bytes every run.
"""

import os

# Setup: the shared ride, the unpressed button, the silence.
SETUP = (
    "So… we both pressed fourteen, neither of us pressed door close, "
    "and now we are just standing here silently calculating the odds "
)
# Turn: the unspoken blame, sniffed out by a machine nose.
TURN = "that one of us is why this elevator smells faintly of warm plastic."

LINE = SETUP + TURN

MAX_CHARS = 200


def build_line() -> str:
    """Assemble the entry line and guard the competition's gate."""
    line = LINE.strip()
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"entry line is {len(line)} chars, gate is 1-200")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build_line())


if __name__ == "__main__":
    main()
