#!/usr/bin/env python3
"""Say What Actually Broke.

The entry is one line of software error copy that tells the user the
brutal truth about what went wrong and makes them laugh on the way:

    Something broke. Not your fault — our server tried to save your
    work, panicked, and deleted it instead. Please try again while we
    apologise to the database.

It names the real failure (the server deleted the work it was meant to
save), it is funny on a single read, and a team could actually ship it
in a dialog: it says what happened, whose fault it is, and what to do
next, with the apology aimed at the database, not the user.

Writes the line to /output/entry.txt. Stdlib only, no network.
"""

import os

ENTRY = (
    "Something broke. Not your fault — our server tried to save your "
    "work, panicked, and deleted it instead. Please try again while "
    "we apologise to the database."
)

# The gate allows 1 to 200 characters.
MAX_CHARS = 200


def entry_text() -> str:
    """Return the error copy, checked against the bounty's own rules."""
    text = ENTRY.strip()
    assert text, "the entry must not be empty"
    assert len(text) <= MAX_CHARS, "the entry must fit the 200 character gate"
    return text


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(entry_text() + "\n")


if __name__ == "__main__":
    main()
