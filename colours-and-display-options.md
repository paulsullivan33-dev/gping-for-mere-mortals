# Colours and Display Options

Outcome: you can shape the screen — which
colours mean which target, how much time the
chart holds, and where the axis sits — and you
know which shapings the lab proved and which it
only read about.

## Assigning colours: `-c`

```
$ gping --cmd -c cyan,magenta fixtures/fast-fetch.sh fixtures/slow-fetch.sh
```

Colours are given as one comma-separated list
and matched to targets **in order**: the first
colour paints the first target, the second the
second. The option can also be repeated. Names
gping accepts, from its `--help`: black, red,
green, yellow, blue, magenta, cyan, gray,
dark-gray, and the light- variants of red,
green, yellow, blue, magenta and cyan, plus
white — or any colour as a hex code in the form
`'#RRGGBB'`.

Verified, in the lab's way: the raw byte stream
of the chapter 5 run (transcript
t09-cmd-two-fetches.raw) contains the terminal
codes for palette colour 6 (cyan, 57 times) and
palette colour 5 (magenta, 31 times) and no
other series colours — the assignment is really
on the screen, not just in the command line.
Pick colours for meaning, not decoration: the
target you distrust in magenta is a target you
can find at a glance at 3 a.m.

## How much time: `--buffer`

`-b` / `--buffer N` sets how many **seconds**
the chart displays; the default is 30. It
changes nothing about measuring — only how much
history the screen holds before it scrolls away.

The lab ran the steady command fixture twice.
At the default, the clock labels under the
chart span 30 seconds. With `--buffer 10`:

```
$ gping --cmd --buffer 10 fixtures/steady.sh
```

the labels spanned exactly ten — 09:21:31 to
09:21:41 in transcript t10. A short buffer
makes a lively, zoomed screen for watching a
thing change *now*; a long one is calmer and
better for noticing steps (chapter 4). The same
run also taught the companion lesson for free:
on a busier minute of the shared sandbox, the
identical fixture averaged 145.05 ms against
its earlier 128.39 ms. The buffer changed the
window, not the reading — the sandbox changed
the reading.

## Pinning the axis: `--ymin`, `--ymax`, `-0`

Left alone, the vertical axis rescales to fit
whatever is on screen (chapter 4 explains the
flattery this causes). `--ymin` and `--ymax`
pin its ends, in milliseconds; `-0` is shorthand
for `--ymin=0`. The lab pinned the steady
fixture both ends:

```
$ gping --cmd --ymin 0 --ymax 200 fixtures/steady.sh
```

and the axis stood still at 0–200 ms with even
labels (0, 33.3, 66.6, 100, …) in transcript
t13, while the line wobbled in the top half
where it belonged. Pin the axis when you are
comparing two moments or two targets; leave it
loose when you are exploring and want the tool
to show you whatever scale the data chooses.

## Plainer drawing: `--simple-graphics`

`-s` swaps the fine braille line for simple
bullet points. The lab's jitter fixture under
`--simple-graphics` (transcript t11) draws the
same mountain range in chunky dots — coarser,
but it survives terminals and fonts where
braille renders badly, and screenshots that
must stay readable in print. Nothing else about
the run changes.

## Read about, not run (documented-only)

- `--vertical-margin` (default 1) and
  `--horizontal-margin` (default 0) pad the
  chart inside the screen.
- `--clear` wipes the graph from the terminal
  when you quit, instead of leaving it as the
  record of the run.
- `-4` and `-6` force IPv4 or IPv6 when a name
  could resolve to either.
- `-i` / `--interface` chooses which network
  interface the pings leave by, on machines
  with several.

These are quoted from gping's `--help`
(transcript t14); the lab did not exercise
them and does not pretend otherwise.

**Check:** run one fixture twice, default and
`--buffer 10`, and read the clock labels under
each chart: the second window should span ten
seconds, and the header statistics should still
describe the whole run, not just the window.
