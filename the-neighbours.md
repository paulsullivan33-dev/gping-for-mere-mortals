# The Neighbours

Outcome: for any "is it slow, is it down" job,
you can name the tool whose question matches
yours. These are characterisations, not
benchmarks — the lab ran gping, not a contest.

**ping** — the parent. One line per reply,
numbers scrolling away, a summary when you stop
it. Everything gping knows in ICMP mode comes
from ping's own mouth (chapter 9); gping adds
memory and shape. For a single quick "is it
alive and roughly how far", plain ping is still
the fastest question in the building.

**mtr** — ping's path-aware relative: it probes
hop by hop and reports loss and time *per
router along the way*, answering the "where"
question gping cannot. When a gping watch says
"something out there", mtr is the natural next
tool. (No guide in this series covers mtr; it is
named here because an honest map of the
neighbourhood includes it.)

**hping3** — a craftsman's packet tool: it
builds TCP, UDP and ICMP probes to order, for
firewalls and odd corners. Powerful, sharp, and
meant for people who already know which packet
they wish existed. Not a watching tool.

**A speed test** — answers a different question:
not "how long until an answer" but "how much
can the pipe carry". A connection can ace one
and fail the other; a fast download says
nothing about jitter, and a sick call is rarely
a bandwidth problem.

**Your service's own logs and health pages** —
the top floor of chapter 1's building. gping
can tell you the network answered in 160 µs
while the application wrote errors for an hour.
When the graph and the logs disagree, believe
both: they were never measuring the same thing.

**The watchers in this series** — *Suricata for
Mere Mortals* watches network traffic for
trouble of the hostile kind; *bandwhich for
Mere Mortals* shows which of your own processes
are using the bandwidth. gping's question is
narrower and older than either: *how long did
the answer take, and did it come at all?*

**Check:** for each tool above, state its
question in five words or fewer. If two of them
share a question in your summary, reread —
they do not.
