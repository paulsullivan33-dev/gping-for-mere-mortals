# Writing criteria for this guide

Every "for Mere Mortals" guide is written to the same nine-point
standard, so a reader who trusts one can trust the rest. Here it
is, with the verification notes for this particular guide below.

1. **Fix it first.** Reader outcomes lead, not action items: each
   chapter opens by naming the outcome it delivers, shows a check
   the reader can run to confirm they got it, and a reasonable
   reader finishes able to state what was done, what it means,
   and what to try next.
2. **Plain language.** Short sentences, everyday vocabulary,
   technical terms defined on first use. No slang, and no
   idioms that only make sense in one country — the reader may
   be translating as they go.
3. **No dead ends.** A guide never tells the reader to do
   something it cannot show them how to verify. Every claim a
   reader relies on — an install, a command, an output — is
   something this guide demonstrates or clearly labels
   documented-only below.
4. **Live-verified where it matters.** Procedures are run for
   real in the guide's lab wherever the build machine allows it,
   and the transcripts kept in the repository are the evidence.
   What could not be run is listed honestly below, never
   presented as if it had been.
5. **General audiences.** Nothing in this guide — examples,
   fixtures, names, addresses — is modelled on any particular
   reader or author's real life, network, or organisations.
   The lab's traffic is the lab talking to itself.
6. **Standalone.** A reader needs this guide, its lab, and
   nothing else. Where another guide would genuinely help, it
   is pointed to once, by name, and the chapter still completes
   without it.
7. **Honest about limits.** The limits chapter names what the
   tool cannot do: a graph that reaches only the floor it is
   pointed at — network stack, handshake, or one command's
   duration — and is silent about the application above it; a
   default TCP setting that counts a dead service's refusals
   as replies; sampling that lets short events slip between
   probes; statistics that remember what the chart forgets;
   an axis that rescales its own opinion; command timings with
   the measuring machine's load baked in; and no logging, no
   history, no alerts once you press q.
8. **The one rule is in the text, early.** Chapter 1 and the
   README state the rule plainly — *a reply proves the other
   machine's network answered, not that the service you care
   about is working* — before any procedure depends on it, and
   later chapters point back to it where the graph could be
   mistaken for a verdict: the healthy TCP graph of a slow
   server, the serene graph of a dead one, the flat graph
   offered as a guarantee.
9. **Builds clean.** The site builds with MkDocs in strict mode
   with no warnings, and a fresh reader following the chapters
   in order reaches the stated outcome of each.

## Verification notes for this guide

The build machine is a 4-CPU Ubuntu 24.04 sandbox (kernel
7.0.0-39), shared with other work, so its load — and therefore
some of the lab's numbers — varies between runs; where that
happened the chapters say so over the figures themselves.
gping **1.21.0** was the project's official release binary
(`gping-Linux-gnu-x86_64.tar.gz` from the orf/gping GitHub
releases), run from a scratch folder rather than installed
system-wide; the companions were iputils ping 20240117,
Python 3.12.3 and curl. The sandbox **refuses ICMP outright**:
its capability bounding set contains no cap_net_raw and no
cap_net_admin, the ping-socket group range is empty
(65534 65534), ping carries no file capability, and both the
system ping and a two-line Python socket attempt to 127.0.0.1
were refused (t01). gping's ICMP mode on Linux runs the system
ping, so ICMP graphing could not be run in this lab at all;
its TCP and --cmd modes need nothing the sandbox withholds,
and everything they do was run for real. Because gping is a
full-screen display, runs were driven under a pseudo-terminal
by `gping-lab/pty-run.py` (100×32), which records the raw byte
stream and presses q at the end; `gping-lab/render.py` rebuilds
the final screen from those bytes with the pyte terminal
emulator, and the .txt transcripts are those screens, with the
.raw bytes kept beside them. Midway through the build the
sandbox emptied /tmp without warning, taking the first binary
and helper environment with it; the lab moved its scratch into
the workspace and re-made the two captures that had not yet
been rendered, which is why transcripts t08 onwards come from
the second sitting.

Run for real, with transcripts as evidence:

- Version, the full `--help` text, and the companion versions
  (t00, t14). The help is quoted throughout the guide rather
  than paraphrased: watch intervals (0.2 s ping, 0.5 s cmd),
  the 30-second default buffer, the TCP refusal wording.
- The permission evidence, complete (t01): group range, the
  system ping's `socket: Operation not permitted`, Python's
  datagram refusal (Errno 13) and raw refusal (Errno 1),
  getcap's silence, and the bounding set decoded — only
  cap_net_bind_service and cap_net_broadcast of the cap_net_*
  family are in it.
- gping's ICMP attempt (t02): `gping 127.0.0.1` printed
  "There was an error running ping: exit status: 2" with
  ping's stderr quoted, and exited — the proof that gping on
  Linux speaks through ping.
- TCP mode against the fixture server, up (t03): header —
  last 638µs, min 104µs, max 1.037ms, avg 186µs, jtr 87µs,
  p95 483µs, t/o 0 — while curl's stopwatch, in the same
  sitting, read 0.307 s on the same server's slow page and
  0.0017 s on its fast page (t15). Chapter 1's rule is
  those three numbers.
- TCP mode, server killed eleven seconds into a 26-second
  run with `--tcp-rst drop` (t04): healthy statistics
  (avg 221µs) frozen in the header, the line gone, last 0ns,
  t/o 74.
- TCP mode, server down throughout, default `--tcp-rst pong`
  (t05): last 160µs, avg 160µs, t/o 0 — a healthy graph of
  nothing but refusals.
- TCP mode against the deaf fixture (listens, never accepts)
  (t06): first readings 111–120µs from the backlog queue,
  then silence; t/o 54, last 0ns.
- Command mode, steady fixture (sleep 0.12) (t07): last
  146.8ms, min 121.95ms, max 164.36ms, avg 128.39ms,
  jtr 9.335ms — the recipe plus its starting costs, itemised
  in chapter 7.
- Command mode, jitter fixture (random 0.04–0.29 s sleeps)
  (t08): min 89.096ms, max 294.61ms, avg 192.24ms,
  jtr 70.399ms.
- Two commands on one chart with `-c cyan,magenta` (t09):
  fast-fetch avg 48.254ms, slow-fetch avg 351.42ms; the raw
  stream carries palette colour 6 (cyan) 57 times and colour
  5 (magenta) 31 times, and no other series colours.
- `--buffer 10` (t10): the chart's clock labels span exactly
  ten seconds against the default runs' thirty; the same
  steady fixture averaged 145.05ms in that busier minute,
  quoted in chapter 6 as the measuring machine's weather.
- `--simple-graphics` (t11): the jitter range drawn in bullet
  points instead of braille. That run's readings ran high
  (max 520.31ms) under the sandbox's load; chapter 6 and the
  limits chapter use the fact rather than hiding it.
- `--ymin 0 --ymax 200` (t13): the axis pinned at 0–200ms
  with even labels, the line riding in its top half.
- The error paths (t12): no arguments — "At least one host
  or command must be given", exit code 1; `--cmd false` —
  an empty chart with only the timeout row, proving failed
  runs count as timeouts; a run at a nonexistent host name,
  which in this sandbox meets the permission refusal before
  name resolution is ever reached, and is described as such.

Documented only — described from the project's documentation
or `--help` text, not run, and the text does not claim
otherwise:

- **ICMP graphing itself** — multiple hosts on one chart,
  live remote targets, the cloud shorthand targets such as
  aws:eu-west-1. The screen, header and statistics are the
  same ones the lab proved in TCP and command modes; the
  ICMP feed for them could not run here (see above), and
  every ICMP-specific passage is written to say no more than
  ping's own behaviour and gping's help support.
- Installation routes other than the release binary: cargo,
  Homebrew, winget, Scoop, Chocolatey and distribution
  packages.
- `--vertical-margin`, `--horizontal-margin`, `--clear`,
  `-4` / `-6` and `--interface`: quoted from `--help`, not
  exercised.
- Behaviour on macOS and Windows, including the different
  default watch interval on OpenBSD the help mentions.
- The neighbouring tools in chapter 11 are characterised,
  not benchmarked; mtr and hping3 are named from general
  knowledge because an honest map of the neighbourhood
  needs them.

Fixtures are this guide's own and deliberately generic: a
two-page web server with a fast page and a slow one, a
listener that never accepts, a script that sleeps a fixed
twelfth of a second, one that sleeps at random, and two
one-line fetches. Every target is 127.0.0.1; no example is
modelled on any real person, network, service or
organisation.
