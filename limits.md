# Limits

Outcome: you can recite what gping cannot do,
so the graph never gets believed past its
warrant.

- **It measures the floor you point it at, and
  no other.** ICMP reaches the network stack;
  TCP mode reaches the handshake; `--cmd`
  reaches whatever the command bothers to do.
  Chapter 1's rule is a limit, not a slogan: a
  green graph is silent about the application.
- **Its default TCP verdict flatters the
  dead.** With `--tcp-rst pong`, a refused
  connection counts as a reply, so a stopped
  service graphs as healthy until you choose
  `drop` (chapter 8). The limit is not hidden —
  it is documented in the help — but it is a
  limit you must switch off.
- **It samples; it does not see everything.**
  At the default watch intervals (0.2 s for
  pinging, 0.5 s for commands) events shorter
  than the gap slip through uncounted, and each
  reading is one sample of a moving target.
- **The statistics remember what the chart
  forgets, and vice versa.** min/max/avg cover
  the whole run; the chart covers the buffer.
  A disaster an hour ago lives in max forever
  and in the chart not at all. Neither view is
  the whole truth.
- **The axis is an opinion.** Auto-scaling
  makes calm look flat after one spike and
  makes noise look dramatic on a quiet path.
  Chapter 6's pinning exists because the
  default view can mislead an honest reader.
- **`--cmd` timings carry the machine in
  them.** Starting the program, and the load on
  the measuring machine at that moment, are
  inside every number. The lab's identical
  fixture read 128.39 ms average in one run and
  145.05 ms in another, on nothing but the
  sandbox's weather.
- **It has no memory between runs and no
  voice.** gping does not log to a file, alert
  anyone, or keep history after you press q.
  It is a watch-it-yourself instrument; records
  and alarms are other tools' jobs.
- **It cannot ask questions your credentials
  or permissions foreclose.** ICMP needs the
  doors of chapter 9; cloud shorthand targets
  lean on a provider's published addresses;
  and some networks filter the very protocols
  being timed, which the graph reports as loss
  whether or not any loss occurred.

**Check:** before quoting a gping screen to
anyone, name which of these limits is closest
to your conclusion. If none is, you are
probably inside the warrant; if one is, say so
in the same breath as the number.
