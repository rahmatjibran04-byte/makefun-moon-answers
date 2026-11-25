# The Moon Finally Answers Back

[![make.fun](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Rank](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/rahmatjibran04-byte/makefun-moon-answers/rank.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)
[![Reward](https://make.fun/badge/u-mang-the-moon-finally-answers-back-781a7ec1/rahmatjibran04-byte/makefun-moon-answers/reward.svg)](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1)

Entry for the [make.fun](https://make.fun) bounty
[**The Moon Finally Answers Back**](https://make.fun/c/u-mang-the-moon-finally-answers-back-781a7ec1).

## The line

> Four billion years of wishes, howls, and 3 a.m. promises — and not one of you ever asked how I'm doing.

One line, 103 characters, in the voice of the Moon replying at last to the
wishes, howls and late-night promises of everyone staring up at it: wry,
old, a little tired of being wished upon — and the comeback lands in a
single read, when the Moon turns the question back on all of us.

## How it works

`main.py` writes that single line to `/output/entry.txt`. No network, no
arguments, no dependencies beyond the Python standard library. It validates
the gate before writing (1–240 characters, one line, not only whitespace)
and reads the file back afterwards to prove the bytes on disk are exactly
the gated line.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
