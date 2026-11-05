# What a Ping Actually Measures

Outcome: you can say, in plain words, what the
three numbers on a ping graph mean — and what
none of them can ever prove.

## The question ping asks

A ping is two small messages. Your machine sends
an **echo request** — "if you can hear this, say
so" — and the other machine's network software
answers with an **echo reply**. No program on the
other side has to be running for this to work;
answering echoes is built into the networking
layer of every operating system. That is ping's
strength and its limit, in one sentence: it tests
whether the other machine's *network stack* is
awake, and nothing above that layer.

The classic tool uses the **ICMP** protocol for
these messages. gping's other two modes, met in
chapters 7 and 8, time a TCP connection opening
or a command running instead — same stopwatch
habits, different question.

## The three numbers

**Round-trip time** is the stopwatch reading for
one request and its reply: out, back, done. It is
usually quoted in milliseconds (ms), and a
thousandth of a millisecond — written µs on
gping's screen — matters on a local network,
where the lab's own loopback replies had a
floor of 104 µs. Round-trip time bundles
everything into one number: the wire, the other
machine's mood, your own machine's mood. It
cannot tell you which part was slow.

**Loss** is the requests that never got a reply
at all. gping counts them as **t/o** (timeouts)
in its header and leaves a gap in the graph.
One lost echo is weather; a rising timeout count
is climate.

**Jitter** is how much the round-trip time jumps
about from one reply to the next. Two targets can
share an average and feel completely different:
the lab's steady fixture averaged 128.39 ms with
a jitter of 9.335 ms — a metronome — while its
jitter fixture averaged 192.24 ms with a jitter
of 70.399 ms, a line like a mountain range. For
anything real-time — calls, games, remote
desktops — jitter is often the number that
decides whether the thing feels broken.

A fourth figure rides along in gping's header:
**p95**, the value that 95 percent of replies
came in under. It is the honest answer to "how
bad does it usually get at worst" — the average
flatters, the maximum exaggerates one moment,
and p95 sits between them.

## The one rule

> **A reply proves the other machine's network
> answered — not that the service you care about
> is working.**

The lab's own evidence, from chapter 8: one
fixture web server, one minute. gping's TCP
graph of that server averaged **186 µs**.
Asking the same server for its slow page with
curl took **0.307 seconds** — more than sixteen
hundred times longer. The server process was struggling
to serve pages while its network stack answered
connection requests almost instantly, because
answering connections is the kernel's job and
needs nothing from the struggling program.

Hold on to that whenever a graph looks healthy
and a user says the thing is down. Both of you
can be right; you are measuring different
floors of the building.

**Check:** you should be able to explain why a
flat, fast graph does not clear a web server of
suspicion — and which of gping's other modes
(chapters 7 and 8) asks the question one floor
higher.
