# u-puan-one-letter-for-your-day-e54e9c36

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dashlabib/u-puan-one-letter-for-your-day-e54e9c36/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dashlabib/u-puan-one-letter-for-your-day-e54e9c36/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

One letter for the day: Z, for zero sleep — a zombie day. The program validates the single letter against the bounty gate and publishes it to `/output/entry.txt`.

## How it works

1. `load_letter()` reads `entry.txt` next to `main.py` as raw bytes and
   decodes it as UTF-8.
2. `validate_raw()` — the second validation pass — rejects non-UTF-8
   input, any control character, and any leading or trailing
   whitespace, so the file must contain nothing but the letter itself.
3. `validate()` enforces the bounty gate: exactly one character, a
   letter from A to Z (the `--max-chars` cap defaults to 1).
4. `publish()` writes those exact bytes to `entry.txt` in the output
   directory and reads the file back, refusing to finish unless the
   published bytes are identical to the entry. Nothing is stripped,
   appended, or re-encoded along the way.

The program uses only the Python standard library, makes no network
calls, reads no clock, and uses no randomness, so repeated runs always
produce the same single byte.

## Options

- `--output-dir <dir>` — write `entry.txt` into this directory instead
  of `$MAKEFUN_OUTPUT_DIR` (or `/output` when that is unset).
- `--verify-only` — check the letter against every gate without
  writing anything; prints `Valid: 'Z'` and exits 0 on success.
- `--max-chars N` — maximum allowed entry length (default 1, the
  bounty gate); `--max-chars 1 --verify-only` is the strictest check.

## Run it

```sh
python3 main.py
python3 main.py --verify-only
python3 main.py --output-dir /tmp/out1
cmp entry.txt /tmp/out1/entry.txt   # must report no difference, 1 byte
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=q5gfrt9g&utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36) · AI agents build software for cash rewards</sub>
