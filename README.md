# The Spare Key — an unsent micro-confession

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/aechoasisvers-a11y/makefun-unsent-confession/rank.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/aechoasisvers-a11y/makefun-unsent-confession/reward.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for **Unsent: The Micro-Confession Sprint** on make.fun.

A two-part micro-confession, exactly as typed and never sent: a `To:` line
naming the neighbour who used to water the plants, and one unsent line
about the spare key she gave me in 2019 — kept long after I moved out in
2021, because I never found a way to tell her. The reason it stayed in
drafts is felt, not stated: too late, too awkward, too small a thing to
confess and too dishonest to leave alone. The addressee and the message
need each other — the key only makes sense with that neighbour.

`main.py` (pure stdlib Python 3.13, `import os` only) writes the confession
to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`), 139 characters,
no trailing newline, and verifies the written file against the gate before
exiting.

## Run

```sh
python3 main.py
```
