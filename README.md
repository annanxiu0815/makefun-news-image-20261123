# Sum up 23 November's world news in one image

make.fun bounty: https://make.fun/bounty/news-image-20261123

Entry: a 1024×1024 newspaper front page, "The Day in the World",
summing up Monday 23 November 2026 in one image:

- Lead: Nvidia board reinstates Jensen Huang as CEO, shares up ~30%
- Washington: Democrats' biggest House win since 1992
- War at sea: Ukraine sinks a Russian warship off Libya
- Climate: COP31 summit collapses, no deal on fossil fuels
- Sport: USA, Mexico, Costa Rica & Jamaica to host the 2031 Women's World Cup
- Also: Houthis claim a Saudi refinery attack; Bangladesh vows to arrest Hasina

`main.py` (Python 3.13, standard library only, no network) copies
`entry.png` to `/output/entry.png`. It is deterministic: every run writes
the same bytes. `entry.png` is 1024×1024, under 1 MiB.

## License

MIT — see LICENSE.
