# Glossary

**Backlog** — the kernel's small queue of
connections that have arrived but not yet been
accepted by the program listening. When it
fills, new connections are left hanging; the
deaf-server fixture in chapter 8 lives there.

**Buffer** — in gping, the number of seconds of
readings the chart displays at once (default
30, set with `--buffer`). What scrolls past is
gone from the chart, though not from the
run's statistics.

**Capability** — a slice of administrator power
that Linux can grant to one program or process
instead of the whole root account.
`cap_net_raw` is the slice that permits raw
sockets; chapter 9 is about its absence.

**Echo request / echo reply** — the ICMP
messages a ping is made of: "say so if you hear
this", and the saying-so. Answered by the
operating system's networking layer itself.

**ICMP** — Internet Control Message Protocol:
the network's own errand channel, carrying echo
requests and replies and several kinds of
error report.

**Jitter (jtr)** — how much successive
round-trip times differ from one another; the
restlessness of a path, quoted by gping as a
single figure in the header.

**p95** — the round-trip time that 95 percent
of replies beat. "Usually, at worst, about
this."

**Ping socket** — an unprivileged kind of ICMP
socket Linux offers to ordinary programs, for
users whose groups fall inside
`net.ipv4.ping_group_range`.

**Refusal (RST)** — TCP's instant "nobody is
listening on that port", sent by the kernel.
Fast, definite, and — under gping's default
TCP setting — counted as a reply.

**Round-trip time (RTT)** — the stopwatch
reading for one probe and its answer, out and
back together. Quoted in milliseconds, or in
microseconds (µs) when it is very small.

**Timeout (t/o)** — a probe that got no answer
inside its waiting time, counted in gping's
header and drawn as the dotted row at the top
of the chart. In `--cmd` mode, a command that
fails counts here too.

**Watch interval** — the pause between probes:
0.2 seconds by default for pinging, 0.5 for
commands, set with `--watch-interval`.
