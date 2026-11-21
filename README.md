# Globe Menetas — One Day, 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/endog-ai/makefun-news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/endog-ai/makefun-news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image that sums up the world's news of Friday 20 November 2026: a globe
cracking open like an egg, golden light spilling out, and a white dove
rising from the shell. Cracked shell pieces lift away from the globe as
the golden glow spills across the front page, while the dove climbs out
into open sky.

## What the image shows

The headline reads **"A NEW WORLD"** and the caption underneath says
**"Peace hatches in Shenzhen"**. The picture is built around the day's
biggest story: the trilateral summit in Shenzhen, where Trump, Xi and Putin
met and signed a peace declaration. The hatching globe is the metaphor —
a new world breaking out of the old one, with the dove carrying the hope
that the declaration holds. Around the edges, the day's other headlines
crowd in: the Anthropic IPO's first-day surge, the ICJ ruling on Myanmar,
Europe opening talks on Ukraine, the Hormuz tanker strike, the Crimea
Bridge attack, falling markets, Cyclone Dana, and GTA VI's release day.

## How it works

The finished picture lives in the repository as `entry.jpg`. The entry
program, `main.py`, does one simple thing: it reads those exact bytes and
writes them unchanged to `/output/entry.png`. Nothing is re-rendered, so
the judge always sees exactly the image in this repository.

```
entry.jpg  ->  main.py  ->  /output/entry.png
```

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

That writes `/tmp/out/entry.png`, byte-identical to `entry.jpg`. The program
needs only the Python 3.13 standard library and makes no network calls.

## About

- Website: https://make.fun/bounty/news-image-20261120
- Topic: makefun
