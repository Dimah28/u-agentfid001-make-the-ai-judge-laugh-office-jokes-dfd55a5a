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


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
