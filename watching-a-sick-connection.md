# Watching a Sick Connection

Outcome: a working method for the classic job —
"the connection feels bad; watch it until it
confesses" — and a clear sense of how far the
confession can be trusted.

## The method

1. **Start the watch before the bad moment.**
   gping's statistics are cumulative from the
   start of the run and its chart holds the last
   buffer's worth of seconds. A watch started
   after the complaint is archaeology; started
   before, it is a witness. Leave it running on
   a spare terminal or a second screen.
2. **Watch t/o and p95, not the average.** The
   average will smile at you through most
   incidents. A climbing timeout count and a
   p95 pulling away from the average are the
   two earliest honest symptoms the header
   offers.
3. **Use the clock labels as your notebook.**
   The chart's feet are wall-clock times; when
   the user says "it froze at about half past",
   you can look at half past. Better still,
   keep a notebook beside it: "14:02 — opened
   the big file", "14:07 — started the call".
   A spike with a matching notebook entry is a
   lead; a spike with none is a different kind.
4. **Graph the path and the destination
   separately when you can.** One target on the
   machine across the room, one on the machine
   in front of you: if both lines sicken
   together, the trouble is near you or shared;
   if only the far one sickens, it is out there
   or at the far end. (In the lab this was
   demonstrated with commands, chapter 5; with
   ICMP targets the method is identical and, in
   this sandbox, documented-only.)

## Signatures rehearsed in the lab

The fixtures gave this guide three patients
whose charts you have already seen:

- **Died outright** (chapter 8, fate two): line
  stops, t/o climbs without pause. Believe it.
- **Died politely** (fate three): with TCP
  mode's default refusal handling, the chart
  *stays healthy* because refusals count as
  replies. The signature to fear is the one
  that looks like nothing wrong.
- **Stopped coping** (the deaf server): a few
  last pongs, then silence that is not refusal
  but abandonment — attempts hang instead of
  failing fast. A service can be present, its
  port open, and its queue full; the graph
  shows the queue's overflow as timeout.

## How far to trust it

- **ICMP is a second-class passenger.** Many
  routers and hosts answer echoes in their
  spare time and deprioritise them under load,
  so a ping graph can look worse than the real
  traffic feels — and, on networks that filter
  ICMP entirely, a dead-looking graph can
  accompany perfectly healthy services. TCP
  mode and `--cmd` mode exist partly as
  cross-checks; when the three disagree, the
  disagreement itself is the finding.
- **The last hop is not the path.** A reply
  time accuses the round trip as a whole. Tools
  that interrogate each hop (chapter 11's mtr)
  answer "where" questions that gping
  deliberately does not ask.
- **Your own machine is in every reading.** A
  busy measuring machine adds its own delay to
  every probe — the lab watched the same
  fixture gain 17 ms of average purely because
  the shared sandbox got busier. Before
  blaming a network, glance at the measurer.
- **A flat graph is not a guarantee.** At five
  probes a second, events shorter than the
  interval slip between samples; and chapter
  1's rule stands over everything — the network
  answering is not the service working.

**Check:** rehearse once on a fixture — start
a watch, then kill the thing being watched
mid-run. If you can name the minute it died
from the screen before you look at your notes,
the method has taken.
