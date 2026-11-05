#!/usr/bin/env python3
"""Run a command under a pseudo-terminal for a fixed number of seconds,
save every byte it prints, then press q to end it (Ctrl-C, then SIGKILL,
if q is not enough).

Usage: pty-run.py RAW_OUT SECONDS -- command [args...]

The terminal is 100 columns by 32 rows. The raw byte stream is what the
program really sent; render.py in this folder turns it back into the
screen a person would have seen.
"""
import fcntl
import os
import pty
import select
import signal
import struct
import sys
import termios
import time


def main() -> None:
    out_raw = sys.argv[1]
    duration = float(sys.argv[2])
    cmd = sys.argv[4:]

    pid, fd = pty.fork()
    if pid == 0:
        os.execvp(cmd[0], cmd)

    # 32 rows, 100 columns — set before the program draws in earnest.
    fcntl.ioctl(fd, termios.TIOCSWINSZ, struct.pack("HHHH", 32, 100, 0, 0))

    data = bytearray()

    def drain(timeout: float) -> None:
        end = time.time() + timeout
        while time.time() < end:
            r, _, _ = select.select([fd], [], [], 0.1)
            if fd in r:
                try:
                    chunk = os.read(fd, 65536)
                except OSError:
                    return
                if not chunk:
                    return
                data.extend(chunk)

    drain(duration)

    try:
        os.write(fd, b"q")
    except OSError:
        pass
    drain(0.8)

    done, status = os.waitpid(pid, os.WNOHANG)
    if not done:
        os.kill(pid, signal.SIGINT)
        drain(0.5)
        done, status = os.waitpid(pid, os.WNOHANG)
        if not done:
            os.kill(pid, signal.SIGKILL)
            _, status = os.waitpid(pid, 0)

    with open(out_raw, "wb") as fh:
        fh.write(bytes(data))
    print(f"captured {len(data)} bytes; child status {status}")


if __name__ == "__main__":
    main()
