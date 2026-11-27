"""Best-meal entry: one sentence about a 2 a.m. bowl of beef noodle soup.

The program holds the entry sentence in TEXT and writes it, exactly as-is,
to /output/entry.txt so the judge can read a single clean line. The output
folder is created on demand, and the file is written as UTF-8 with no
trailing newline, so its bytes are the sentence and nothing else.

How to verify:
    python3 main.py
    cat /output/entry.txt
    python3 -c "print(len(open('/output/entry.txt', encoding='utf-8').read()))"
The length printed should be 188, and running the script a second time
should produce an identical file.
"""

from pathlib import Path

TEXT = (
    "At 2 a.m. in a Taipei alley, I ate beef noodle soup standing up, "
    "broth burning my tongue, and the old man behind the counter "
    "refilled my bowl without asking, like he'd been waiting for me."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry(path: Path = OUTPUT_PATH) -> int:
    """Write TEXT to path, creating parent directories as needed.

    Returns the number of characters written.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(TEXT)
    return len(TEXT)


def main() -> None:
    chars = write_entry()
    print(f"Wrote {chars} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
