"""Write the unsent micro-confession to /output/entry.txt.

Pure stdlib Python 3.13. The entry is exactly two parts: a "To:" line
naming who the message was meant for, and the unsent message itself,
one line written exactly as it was typed, with no explanation after it.
"""

import os

ENTRY = (
    "To: the neighbour who waters my plants when I'm away\n"
    "i still have the spare key you gave me in 2019. "
    "i moved out in 2021 and never told you"
)


def check(text):
    """Check the entry against the gate: 1-260 UTF-8 chars, not blank.

    Also verifies the two-part confession structure the judge scores
    first: a "To:" line naming who it was meant for, then exactly one
    message line, written as typed, with nothing after it.
    """
    if not isinstance(text, str):
        raise TypeError("entry must be text")
    if not 1 <= len(text) <= 260:
        raise ValueError("entry must be 1-260 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    if not lines[0].startswith("To: ") or len(lines[0]) <= 4:
        raise ValueError("first line must be a To: line naming the addressee")
    if not lines[1].strip():
        raise ValueError("message line must not be empty")
    if len(lines[1]) > 200:
        raise ValueError("message line must be at most 200 characters")
    return True


def main():
    check(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what actually landed on disk, not just what we intended.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    if written != ENTRY:
        raise ValueError("written entry.txt does not match ENTRY")
    check(written)


if __name__ == "__main__":
    main()
