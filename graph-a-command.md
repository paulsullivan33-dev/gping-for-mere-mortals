# Graph a Command

Outcome: you can point gping at a command
instead of a host, read the resulting graph for
what it is, and build a service check out of
nothing but a fetch and a stopwatch.

## What `--cmd` measures

With `--cmd`, the things you list are commands,
and the graph shows **how long each run of each
command took**, over and over: run, time, plot,
repeat. The default watch interval in this mode
is 0.5 seconds between starts (chapter 2's help
text), against 0.2 for pinging.

The stopwatch covers the whole life of the
command — starting the program is part of the
time, because from where you sit, waiting, it
is. The lab's steady fixture is a script that
sleeps exactly 0.12 seconds; gping's header for
it (transcript t07) read:

```
fixtures/steady.sh   last 146.8ms  min 121.95ms  max 164.36ms
                     avg 128.39ms  jtr 9.335ms  p95 164.36ms  t/o 0
```

The floor, 121.95 ms, is the 120 ms sleep plus
about 2 ms of starting; the average, 128.39 ms,
adds the sandbox's scheduling weather. Teach
yourself to expect that gap on every command
you graph: the recipe is never the whole meal.

## Flat and jagged: the two fixtures

The jitter fixture sleeps a random 0.04–0.29
seconds per run. Its screen (transcript t08) is
the steady screen's opposite — a mountain range
between 89 and 295 ms:

```
fixtures/jitter.sh   last 173.0ms  min 89.096ms  max 294.61ms
                     avg 192.24ms  jtr 70.399ms  p95 294.61ms  t/o 0
```

Put the two headers side by side and jitter is
the teller: 9.335 ms against 70.399 ms. Averages
alone (128 vs 192) would have told you one was
slower; jitter tells you the second one is
*unpredictable*, which for anything interactive
is the worse diagnosis.

## A service check from a fetch

Chapter 5 already showed the working pattern:
a command that fetches a page turns "is the
service all right" into a duration you can
graph. The lab's pair — fast page avg
48.254 ms, slow page avg 351.42 ms, same
server, same minutes — is the shape of it. The
discipline is in choosing the command:

- **Fetch the thing a user fetches**, not a
  health page that answers cheaply while the
  real work queues. The graph can only time
  the command you gave it.
- **Keep the command honest and small.** A
  fetch that downloads a huge file measures
  bandwidth and patience, not responsiveness.
- **Run it from where the users are.** The
  same command graphed from the server itself
  and from across the network answers two
  different questions; both are legitimate, and
  confusing them is not.

## When a command fails

The lab graphed `false`, the command that does
nothing and reports failure (transcript t12):
the screen shows the name, an empty chart, and
the dotted timeout row across the top. A failed
run has no duration worth plotting, so gping
counts it as a timeout — the same mark as a
lost ping. In a service check that is exactly
the semantics you want: a fetch that errors and
a fetch that hangs both belong in the t/o
column, and the graph's job is to make the
*pattern* of them impossible to miss.

**Check:** graph a command you control twice —
once as it is, once with a deliberate delay
added — and confirm the line steps up by about
the delay and the header's min moves with it.
If min does not move, you are not timing what
you think you are timing.
