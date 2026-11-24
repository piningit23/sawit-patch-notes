"""Real-Life Patch Notes: The Comedy Changelog.

Writes one patch-note line (<=160 chars) for a bug in human biology
to /output/entry.txt. Deterministic, Python 3.13 stdlib only.
"""

import os

ENTRY = (
    "v2.4.1: fixed a bug where the human body requested sleep at 3 a.m. "
    "but the brain opened a tab called 'regrets from 2019' instead."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Echo the entry and its length so a local run is easy to verify.
    print(f"{len(text)} chars: {text}")


if __name__ == "__main__":
    main()
