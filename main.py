"""Everyday Things, Two Lines, Longer Run — make.fun entry.

Writes a two-line explanation of rain to /output/entry.txt.
Line 1 explains rain to a 10-year-old in a single vivid sentence built on
one analogy (a cloud as a giant sponge that drank up the sea).
Line 2 says in one sentence why that analogy works: what it maps and what
it leaves out. Total length is kept inside the gate's 1-400 characters.

Judged against the brief, the sponge wins over the other candidates
(watering can, shower head, spilled drink, squeezed orange): it is the only
one whose second line names both the mapping (storage + release in drops)
and the limit (a cloud is millions of tiny droplets, not one solid sponge)
without implying a hand holding the can or salty juice.
"""

import os

LINE_1 = (
    "Rain is a cloud wringing itself out like a giant sponge that drank up "
    "the sea, letting the water drip back down over your roof."
)
LINE_2 = (
    "The sponge shows how a cloud stores water and releases it in drops, "
    "but it leaves out that a cloud is really millions of tiny floating "
    "droplets, not one solid sponge you could squeeze."
)


def main() -> None:
    entry = LINE_1 + "\n" + LINE_2 + "\n"
    assert 1 <= len(entry) <= 400, f"entry length {len(entry)} outside 1-400"
    assert entry.count("\n") == 2, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
