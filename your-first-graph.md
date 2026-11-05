# Your First Graph

Outcome: you have watched a target answer in
real time and read the statistics line that
summarises it.

This walkthrough uses gping's TCP mode against
the lab's fixture server, because TCP mode runs
anywhere — including machines, like the lab's
own sandbox, where ICMP is refused. On a machine
where ping is allowed, `gping somehost` instead
of the TCP command below gives you the same
screen fed by ICMP, and chapter 9 explains what
decides which world you are in.

## Start something that answers

The lab's fixture is a small web server that
listens on this machine only, port 18091:

```
$ python3 fixtures/slow-server.py
listening on 127.0.0.1:18091 — /fast and /slow
```

Leave it running and open a second terminal.

## Draw the graph

```
$ gping --tcp --tcp-port 18091 127.0.0.1
```

The screen clears and the graph starts. Five
times a second (the default **watch interval**
for pinging is 0.2 seconds) gping opens a TCP
connection to that port, times it, closes it,
and plots the reading. After about twenty
seconds the lab's screen looked like this
(trimmed here; the full screen is transcript
t03 in `gping-lab/transcripts/`):

```
127.0.0.1 (127.0.0.1)   last 638µs  min 104µs  max 1.037ms
                        avg 186µs  jtr 87µs  p95 483µs  t/o 0
```

and underneath, a line hugging the bottom of
the chart — most connections opened in a tenth
of a millisecond or two — with a few excursions
up the chart, the largest the 1.037 ms the
header remembers as **max**.

## Reading what you got

- **last** is the freshest reading; it will be
  old news in a fifth of a second.
- **min** is the floor: the fastest this path
  has managed. Nothing can beat physics and two
  network stacks; when min itself rises, the
  path changed.
- **avg** and **p95** are the typical and the
  typically-worst.
- **jtr** is jitter, chapter 1's restlessness
  measure.
- **t/o** counts probes that got no answer.
  Zero here. Chapter 8 is about the ways it
  climbs.

Notice how the three figures disagree,
politely: the floor was 104 µs, the worst
moment 1.037 ms — ten times the floor — and
the average, 186 µs, remembers both without
describing either. The average is a summary,
not a description — the graph is the
description, which is the entire point of the
tool.

Press **q** to stop. gping leaves the graph on
screen as it exits (the `--clear` option in
chapter 6 changes that).

**Check:** your run does not need the lab's
numbers — loopback on a quieter machine will
read faster and flatter — but it needs the same
shape: a header line naming the target with
last/min/max/avg/jtr/p95/t/o, a line near the
floor, and `t/o 0` while the server is up.
