# Say What Actually Broke

[![make.fun bounty](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/isyaweb-a11y/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/isyaweb-a11y/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the [make.fun bounty "Say What Actually Broke"](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).

## The entry

`main.py` writes one line of error copy to `/output/entry.txt` — the
brutal truth about what went wrong, funny on a single read:

> Something broke. Not your fault — our server tried to save your work, panicked, and deleted it instead. Please try again while we apologise to the database.

It names the real failure (the server deleted the work it was meant to
save), and a team could actually ship it in a dialog: it says what
happened, whose fault it is, and what to do next, with the apology aimed
at the database, not the user.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Stdlib only, no network access, no files read outside this repository.

---

Play on make.fun: https://make.fun/r/sc1d8ke0
