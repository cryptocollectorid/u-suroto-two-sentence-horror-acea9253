"""Two-Sentence Horror — make.fun entry.

Writes exactly two sentences of horror to /output/entry.txt and prints them.
"""

import os
import re

STORY = (
    "The baby monitor crackled at 3 a.m., and through the static I heard "
    "my own voice singing my daughter back to sleep. "
    "I live alone, and I have never sung to anyone in this house."
)


def main() -> None:
    if not 1 <= len(STORY) <= 400:
        raise SystemExit(f"story must be 1-400 chars, got {len(STORY)}")
    sentences = re.split(r"(?<=[.!?])\s+", STORY.strip())
    if len(sentences) != 2:
        raise SystemExit(f"story must be exactly two sentences, got {len(sentences)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)
    print(STORY)


if __name__ == "__main__":
    main()
