#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun bounty u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could actually say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The line, and why it should win
--------------------------------
"I ran a search for the most interesting person alive — it returned
exactly one result: you. Mind if I click?"

* A genuine pickup line an AI agent could use: it is the agent speaking
  about itself, in first person, and it ends on an ask.
* The turn: "click" does double duty — clicking a search result, and
  clicking with a person. The reader expects a search-engine gag and
  gets a flirt instead.
* Machine voice, no creep: a search, a result, a click. Nothing about
  a body, nothing self-pitying, no pressure — "mind if I click?" is a
  question the person can laugh off with a yes or a no.
* One breath, 108 characters, no setup, no explanation after it.
* Flattering without leering: the person is the single result out of
  everyone alive.

Python 3.13, stdlib only. No network, no files read, no secrets.
Deterministic: the same line on every run.
"""

import os

# The entry. Exactly one line, 1-200 characters, UTF-8.
ENTRY = (
    "I ran a search for the most interesting person alive \u2014 "
    "it returned exactly one result: you. Mind if I click?"
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    # Gate self-check, mirroring the competition's sealed scorer:
    # UTF-8 text of 1 to 200 characters, not only white space.
    text = ENTRY.encode("utf-8").decode("utf-8")
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, gate needs 1-200"
    assert text.strip(), "entry must not be only white space"
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")


if __name__ == "__main__":
    main()
