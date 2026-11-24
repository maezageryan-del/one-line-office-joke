#!/usr/bin/env python3
"""One-Line Office Joke — make.fun entry.

Prints one single-line joke about office life (145 characters, well under
the 200-character limit) and writes the exact same text to
/output/entry.txt, where the bounty harness reads it.
"""

import os

JOKE = "I expensed a coffee as 'client relationship development' and finance approved it, so my caffeine addiction is now officially a business strategy."


def main():
    # Gate guard: the bounty refuses any entry over 200 characters, so
    # fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(JOKE) <= 200:
        raise ValueError(f"joke must be 1-200 characters, got {len(JOKE)}")
    print(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
