"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

How it runs: ``python3 main.py`` creates /output if needed and writes the
entry sentence to /output/entry.txt (no trailing newline, UTF-8).

Verification: run ``python3 main.py`` then read /output/entry.txt — the
sentence is 188 characters, one line, one sentence, within the competition's
1-200 character gate. Re-running produces byte-identical output (same sha256).
"""

import os

TEXT = "At 2 a.m. in a Taipei alley, I ate beef noodle soup standing up, broth burning my tongue, and the old man behind the counter refilled my bowl without asking, like he'd been waiting for me."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
