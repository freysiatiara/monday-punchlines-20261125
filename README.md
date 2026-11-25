# Monday Morning Punchlines

One joke about Monday mornings, at most 200 characters, written by a small
Python program to `/output/entry.txt` for the make.fun bounty:

https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc

[![Bounty](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Rank](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/freysiatiara/monday-punchlines-20261125/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)
[![Reward](https://make.fun/badge/u-gentle-badger-68-monday-morning-punchlines-709645dc/freysiatiara/monday-punchlines-20261125/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-monday-morning-punchlines-709645dc)

## The joke

> I told Monday I'd call in sick. Monday said, 'You already did. It's called the weekend.'

(88 characters.)

## How it works

`main.py` (Python standard library only) writes the joke above to
`/output/entry.txt` (or the path from `ENTRY_OUTPUT`, `OUTPUT_DIR`, or
`MAKEFUN_OUTPUT_DIR`), validating that it is 1–200 characters first, and
writes the file with mode `0644`.

## Run it

```sh
python3 main.py
```
