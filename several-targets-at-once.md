# Several Targets at Once

Outcome: you can put two or more targets on one
chart, keep them straight, and compare them
without lying to yourself.

## The shape of it

Give gping more than one target and it gives
each its own line on the shared chart and its
own line in the header:

```
$ gping host-a host-b host-c
```

— ICMP mode, on a machine where ping is allowed.
The lab's sandbox refuses ICMP (chapter 9), so
the lab demonstrates the identical screen in
`--cmd` mode instead: two fixture commands, one
fetching the fixture server's fast page, one
fetching its slow page, on one chart for 22
seconds (transcript t09):

```
fixtures/fast-fetch.sh   last 99.03ms  min 9.339ms  max 114.71ms
                         avg 48.254ms  jtr 32.639ms  p95 111.32ms  t/o 0
fixtures/slow-fetch.sh   last 388.2ms  min 310.03ms  max 455.29ms
                         avg 351.42ms  jtr 32.388ms  p95 455.29ms  t/o 0
```

On the chart the slow fetch rode along the top
band and the fast fetch scribbled near the
floor — two floors of the same building,
measured by the same stopwatch in the same
minutes, which is what makes the comparison
mean anything.

## Keeping them straight

Each target gets a colour, in the order you
listed them, from gping's rotation; chapter 6
shows how to assign your own with `-c`. Colours
are matched to targets **by position**, and the
header always names which line is which, so
when two lines cross and tangle — as the fast
fetch's excursions tangled with the slow
fetch's floor in the lab run — the header's
statistics are the referee.

## Comparing honestly

- **Same window, same machine.** Averages from
  different runs, at different times, on
  different measuring machines compare the
  weather as much as the targets. Side-by-side
  on one chart is the whole advantage; use it.
- **Compare like with like.** A TCP time and an
  ICMP time to the same host measure different
  floors (chapter 1's rule). Two commands are
  comparable; a command and a ping are cousins,
  not twins.
- **The shared axis serves both.** One wild
  target stretches the scale for everyone
  (chapter 4); pin the axis (chapter 6) when
  the quiet target's wobble is what you are
  actually watching.
- **More targets, more load.** Each ICMP target
  is pinged every watch interval — five times a
  second each, by default. A handful is nothing;
  a hundred is a small flood and a rude one.
  Chapter 10 returns to the politeness of it.

## The cloud shorthand (documented-only)

gping's help mentions targets like
`aws:eu-west-1`, which it resolves through a
cloud provider's published addresses to ping a
region's doorstep rather than a machine of
yours. The lab did not use it — it measures
infrastructure you do not own, from lists
someone else maintains — and this guide simply
notes that it exists.

**Check:** in your own two-target run, cover
the chart and read only the header: you should
still be able to say which target is slower,
which is less steady, and whether either has
lost a probe.
