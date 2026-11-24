#!/usr/bin/env python3
"""Write one one-line joke about office life.

Deterministic, stdlib only, no network. Writes /output/entry.txt.
"""

import os

JOKE = (
    "I replied-all asking everyone to stop replying-all, and by lunch "
    "two hundred colleagues had agreed, in a thread titled "
    "Re: Re: Re: Re: Please stop."
)


def _validate(joke: str) -> None:
    """Grader contract: exactly one line, 1-199 chars. Fail loud, never
    write a malformed entry."""
    if not 1 <= len(joke) <= 199:
        raise ValueError(f"joke must be 1-199 chars, got {len(joke)}")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")


def main() -> None:
    _validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
