# TCP Mode and the Refusal Trap

Outcome: you can time connections instead of
echoes, read a connection graph's three fates,
and never be fooled by the healthy-looking one.

## The mode

```
$ gping --tcp --tcp-port 18091 127.0.0.1
```

Instead of ICMP echoes, gping times **TCP
connections**: each probe opens a connection to
the target's port and stops the clock when the
handshake completes. It exists for the many
networks where ICMP is filtered or refused —
and, not incidentally, it is the ping mode this
guide's sandbox could run at all. `--tcp-port`
chooses the port (default 80).

A connection time measures the kernel at the
far end completing a handshake. The program
behind the port is not consulted — remember
chapter 1's rule, because this chapter is where
it bites.

## Fate one: the server is up

Transcript t03: baseline connections with a
floor of 104 µs, header avg 186 µs, t/o 0.
Meanwhile the same server took 0.307 s to
serve its slow page to curl. The graph was
healthy *and* the service was slow,
simultaneously, in writing.

## Fate two: the server dies mid-run

The lab killed its fixture server eleven
seconds into a 26-second run, with one option
changed — `--tcp-rst drop` (transcript t04):

```
127.0.0.1 (127.0.0.1)   last 0ns  min 113µs  max 766µs
                        avg 221µs  jtr 127µs  p95 570µs  t/o 74
```

The healthy stretch reads beautifully — then
the line stops, the dotted timeout row takes
over the top of the chart, and t/o counts the
silence: 74 unanswered probes by the end. This
is the portrait chapter 4 calls the cliff.

## Fate three: the trap

Run the same dead server **without**
`--tcp-rst drop` — the default is
`--tcp-rst pong` — and transcript t05 shows:

```
127.0.0.1 (127.0.0.1)   last 160µs  min 93µs  max 2.15ms
                        avg 160µs  jtr 82µs  p95 194µs  t/o 0
```

A serene, healthy graph. t/o 0. Nothing was
listening at all.

What happened: with nothing on the port, the
target's kernel instantly **refuses** each
connection (a TCP reset, RST). A refusal is
still an answer from the host — proof it is
awake — so gping's default counts it as a pong,
and its help text says why, in so many words:
*"the host answered, it just isn't listening."*
That is a defensible meaning of "ping". It is
also a trap for anyone watching a *service*:
the graph of a dead service can look better
than the graph of a live one, because a refusal
is faster than a handshake.

The option is the whole lesson:

| Setting | A refusal counts as | Use it when |
|---|---|---|
| `--tcp-rst pong` (default) | a reply | you are asking "is the host awake?" |
| `--tcp-rst drop` | a timeout | you are asking "is the service there?" |

## The fourth state: listening, but gone

The lab's second fixture listens on the port
and then never accepts a single connection
(transcript t06). The first probes complete
from the kernel's small waiting queue —
111–120 µs, three honest pongs — and once the
queue fills, every later attempt hangs
unanswered: line gone, last 0ns, t/o 54 by the
end of the run. That is the signature of a
server that has stopped coping while its
socket still exists: not refused, not answered
— *ignored*. It looks like fate two with a
small false dawn at the start, and on a real
incident that false dawn is often the last
moment the service half-worked.

**Check:** with a fixture of your own, produce
the three headers — up, dead-with-pong,
dead-with-drop — and confirm only the middle
one claims t/o 0. If you cannot make a dead
service look dead, you are watching fate three.
