# gping for Mere Mortals

`ping` is the oldest network question there is:
*are you there, and how long did the answer
take?* It asks politely, prints one line per
answer, and scrolls the evidence away. **gping**
asks the same question and **draws the answers
as a graph**, live, in your terminal — a line
that rides high when replies slow down, breaks
where replies never came, and keeps the summary
statistics (fastest, average, slowest, jitter)
on screen the whole time.

One rule governs everything the graph can tell
you, and this guide states it in chapter 1 and
keeps pointing back to it: **a reply proves the
other machine's network answered — not that the
service you care about is working.** In this
guide's own lab, a fixture web server's TCP
graph averaged 186 µs while that same server
was taking 0.307 seconds to serve its slow page.
Both numbers were true. Only one of them was
about the page.

gping has three ways of asking its question,
and the guide gives each its due:

- **ICMP ping**, the classic: echo requests to
  one host or many at once, five times a second
  by default.
- **TCP ping**, which times how long a
  connection takes to open — for networks where
  ICMP is blocked, and with a trap of its own
  that chapter 8 names and demonstrates.
- **`--cmd` mode**, which graphs how long a
  *command* takes to run: a download, a script,
  a check of your own — the same graph, fed by
  your own stopwatch.

An honest word about this guide's lab, because
it shapes what could be proved in it: the build
machine is a sandbox that refuses ICMP sockets
outright, even to administrators — chapter 9
walks through the refusal and what causes it.
So the ICMP chapters are taught from the ping
tool's own behaviour in that lab and labelled
documented-only where they go beyond it, while
everything the graph itself does — TCP pings,
command timings, colours, windows, axes, the
statistics, and the eloquent empty space where
a dead target used to be — was run for real,
against fixtures the lab built for itself, and
the transcripts are kept in `gping-lab/`.

Nothing in the lab is modelled on any real
network. The targets are the lab talking to
itself.
