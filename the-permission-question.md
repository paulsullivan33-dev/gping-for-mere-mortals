# The Permission Question

Outcome: when ping refuses to run, you can tell
which of the three doors is shut — and in this
guide's lab, you can watch all three refuse.

## Why pinging needs permission at all

An ICMP echo request is a *raw* network packet,
and raw packets are powerful: a program that can
forge them can impersonate other machines. So
operating systems gate them, and the gate has
three common forms:

- **The ping socket.** Modern Linux offers an
  unprivileged kind of ICMP socket, usable by
  ordinary programs — but only for users in
  groups the administrator allows, listed in the
  kernel setting `net.ipv4.ping_group_range`.
- **A capability on the program.** The `ping`
  program can carry the `cap_net_raw` file
  capability — a small, specific grant of the
  raw-socket power, given to that one program
  instead of to its user.
- **Running as root**, historically the original
  door: old ping programs were installed
  set-user-id root for exactly this reason.

gping inherits whichever answer your machine
gives, because on Linux **gping runs the system
`ping` and reads its output** — that is also
what gping's `--ping-args` option feeds. A
gping permission problem is a ping permission
problem wearing a graph.

## The lab's refusal, taken apart

The lab's sandbox shut all three doors, and
each transcript in `gping-lab/transcripts/t01`
is one door:

```
$ cat /proc/sys/net/ipv4/ping_group_range
65534	65534
```

The allowed range is empty — it names a group
range that includes nobody — so the ping socket
door is shut. A direct attempt from Python
agrees: the datagram (ping socket) attempt was
refused with *Permission denied*.

```
$ ping -c 2 -W 1 127.0.0.1
ping: socktype: SOCK_RAW
ping: socket: Operation not permitted
```

ping fell back to a raw socket and was refused
with *Operation not permitted*. `getcap` on the
ping binary printed nothing — it carries no
`cap_net_raw` grant, so door two is shut too.

And door three turns out to be painted on: the
lab ran as root and was still refused, because
the sandbox's **capability bounding set** — the
ceiling no process in it can exceed, however it
got its powers — does not contain `cap_net_raw`
at all. Decoding it (`capsh --decode`, in the
same transcript) lists `cap_net_bind_service`
and `cap_net_broadcast` and then moves on;
`cap_net_raw` and `cap_net_admin` simply are
not there. In such a sandbox no setuid bit, no
file capability and no sudo can mint a raw
socket; the power was never in the building.

Finally, gping itself, given the most innocent
target there is:

```
$ gping 127.0.0.1
There was an error running ping: exit status: 2
Stderr: ping: socktype: SOCK_RAW
        ping: socket: Operation not permitted
```

gping ran ping, ping reported its refusal, and
gping showed it and exited. Notice what did
*not* fail: loopback networking itself worked
all day — TCP connections, the fixture servers,
everything in chapters 3–8. The refusal is
specifically about raw ICMP, not about the
machine being offline.

## On your own machine

- `cat /proc/sys/net/ipv4/ping_group_range` —
  `0 2147483647` is the wide-open setting many
  distributions ship; an empty or narrow range
  is the first suspect when only some users can
  ping.
- `getcap $(which ping)` — shows whether the
  capability door is fitted.
- Plain `ping 127.0.0.1` before gping anything:
  if the parent tool cannot ask, the graph
  cannot either.
- In containers and sandboxes, expect the
  bounding set to be the real answer, and the
  fix to live outside the container, with
  whoever configured it.

Safety, plainly: these grants are small but
real powers. Prefer the ping-socket range or a
file capability over running network tools as
root, and do not loosen a shared machine's
settings to satisfy one graph.

**Check:** in transcript t02, gping's error is
ping's error word for word. Once you can
predict that from this chapter, the next
socket error you meet on any machine is a
diagnosis, not a mystery.
