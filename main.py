#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to /output/entry.txt.
"""

import os

PITCH = (
    "The Hide-and-Seek Remote is a TV remote that dives between the sofa "
    "cushions whenever you raise your voice, and only resurfaces once you "
    "sign a formal apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
