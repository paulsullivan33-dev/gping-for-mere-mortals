# Reading the Graph

Outcome: given any gping screen, you can name
what each part is showing and recognise the
four shapes a sick connection draws.

## The parts

**The header** carries one line per target: its
name (for a host, gping shows the name and the
address it resolved to), then the statistics —
last, min, max, avg, jtr, p95, t/o — defined in
chapter 1 and first met in chapter 3.

**The line** is one target's readings, newest at
the right edge, drawn in fine braille dots so a
small screen can hold a lot of time. With
several targets the lines share the chart and
each keeps its own colour (chapter 5).

**The vertical axis rescales itself.** gping
fits the chart to the readings currently on
screen, so a spike stretches the scale and
squashes everything after it toward the floor
until the spike scrolls away. This flatters and
frightens by turns: a line "going flat" may mean
the target calmed down, or that one bad moment
is still inflating the scale. Chapter 6 shows
how to pin the axis when you want comparisons
to stay honest.

**The horizontal axis is clock time.** The
labels at the bottom are wall-clock times, and
the window they span is the **buffer** — 30
seconds by default. What scrolls off the left
edge is gone from the chart (though min, max
and the counters in the header still remember
the whole run).

**The dotted row at the very top** is the
timeout marker. When probes go unanswered,
gping draws a row of small dots along the top
of the chart — you can see it clearly in the
chapter 8 transcripts — and the t/o counter in
the header climbs. It is the loudest silence
the tool can draw.

## Four shapes worth knowing

**The floor.** A healthy nearby target: a line
scribbling along the bottom with minor wobble.
The lab's steady command fixture (chapter 7)
sat at 121–164 ms around its 120 ms recipe —
the same shape, higher up.

**The spike.** One reading (or a few) far above
the rest, then back to the floor. A spike is a
fact about a moment: something — either end, or
the path, or the machine you are measuring
*from* being busy — was slow just then. The
lab's first TCP run spiked to 1.037 ms — ten
times its own floor — on an otherwise
sub-millisecond path, on a shared sandbox with
other work running. A spike accuses nobody; a
*pattern* of spikes at the same times of day
starts to.

**The step.** The line moves to a new level and
stays there. Steps mean something changed: a
route, a server's load, a Wi-Fi signal's mood.
Steps are why the clock labels matter — "it got
slower at 14:02 and stayed slower" is a report;
"it feels slower" is not.

**The cliff.** The line stops, the dotted row
appears, t/o climbs. Whatever you were measuring
stopped answering. Chapter 8's mid-run kill
shows the exact portrait: statistics frozen
from the healthy minutes, `last` reading 0ns —
there is no last reply — and 74 timeouts by the
end of a 26-second run.

**Check:** in transcript t04 (`gping-lab/
transcripts/t04-tcp-drop.txt`) you should be
able to point at the healthy stretch, the
moment of the cliff, and the header figures
that remember both.
