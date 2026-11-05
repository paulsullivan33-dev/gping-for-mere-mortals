# Troubleshooting

Outcome: the common failures, each with the
symptom you will actually see and the fix that
matches it.

| Symptom | Likely cause | Fix |
|---|---|---|
| `There was an error running ping … socket: Operation not permitted` | Ping itself is refused: empty `ping_group_range`, no `cap_net_raw`, or a sandbox whose bounding set lacks it (chapter 9) | Diagnose ping first with plain `ping 127.0.0.1`; on a machine you administer, widen the group range or grant the capability; in a sandbox, use TCP or `--cmd` mode |
| `Error: At least one host or command must be given` | gping was run with no targets (the lab's transcript t12; exit code 1) | Name at least one host or, with `--cmd`, one command |
| The graph of a stopped service looks perfectly healthy | TCP mode's default `--tcp-rst pong` counts instant refusals as replies (chapter 8) | Add `--tcp-rst drop` when the question is "is the service there" |
| Empty chart, dotted row at the top, t/o climbing from the first second | The target accepts nothing: down, filtered, or listening-but-overwhelmed (the deaf-server pattern) | Check the service itself and its queue; test the same port with a real client (curl) to separate "refused fast" from "hangs" |
| A command-mode graph sits far above the command's own timing | The stopwatch includes starting the program, and your machine's load (chapter 7) | Time the command by hand once for comparison; read min as the floor and expect overhead on top |
| A `--cmd` target shows only timeouts although the command "works" | The command exits non-zero, or fails only in gping's environment (PATH, working directory) | Run the exact command string in the same shell; failed runs count as timeouts by design |
| Two targets' colours seem swapped | Colours bind by position in the argument list, not by name (chapter 6) | Reorder the `-c` list to match the targets, or read the header, which always names each line |
| The line goes flat and unreadable after one spike | The axis auto-scaled to the spike (chapter 4) | Pin it with `--ymin` / `--ymax`, or wait for the spike to scroll out of the buffer |
| Everything reads slower than the same test elsewhere | The measuring machine is loaded; its delay is inside every probe | Check the measurer's own load before blaming the target; compare min, which load inflates least |
| Garbled or missing line-drawing in some terminals | Braille glyphs the terminal or font renders badly | Use `--simple-graphics` (chapter 6) |
| A host name fails while its address works | Name resolution, travelling through ping's own attempt first (in the lab, the permission error arrived before DNS could even be tried) | Test the name with plain `ping`; fix DNS or use the address while you do |

**Check:** every row above except the last was
met in this guide's lab and is tied to a
transcript or a chapter's own run. The mark of
having understood the table is being able to
say, for a new symptom, which row it is
*closest* to — and what you would test before
touching anything.
