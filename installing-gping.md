# Installing gping

Outcome: gping is on your machine, and you have
proved it with its own version line.

## What the lab did (verified)

The lab ran the project's official release
binary, version **1.21.0**: download
`gping-Linux-gnu-x86_64.tar.gz` from the
**Releases** page of the `orf/gping` project on
GitHub, unpack it, and the `gping` inside is the
whole program — one file, no installer. Run from
a folder of your choice, or copied somewhere on
your `PATH` such as `/usr/local/bin` if you have
the rights.

The gnu build is the ordinary Linux one; the
same release page offers `musl` builds (for
Alpine-style systems), ARM builds, macOS, and a
Windows zip.

**Check:**

```
$ gping --version
gping 1.21.0
```

Version numbers will move; the shape of the
answer is what matters.

## Other routes (documented-only)

The project also documents these, which the lab
did not use and this guide does not claim to
have tested:

- **Cargo**, Rust's package tool:
  `cargo install gping` builds it from source.
- **Homebrew** on macOS and Linux:
  `brew install gping`.
- **winget** on Windows:
  `winget install gping`.
- **Scoop and Chocolatey** on Windows, and
  assorted distribution packages — check the
  project's README for the current list, because
  packagings come and go.

Whichever route you take, finish with the same
check: `gping --version` answering with a
version is the whole proof.

## One thing gping needs that it does not carry

On Linux, gping's ICMP mode works by running
your system's `ping` command and reading what it
prints — so `ping` has to exist, and it has to be
*allowed*. In this guide's lab it was not, and
gping said so in ping's own words (chapter 9
takes that refusal apart). TCP mode and `--cmd`
mode are gping's own and need nothing special.
If your first ICMP graph fails with a socket
error, do not debug gping: chapter 9 is the
chapter you want.

**Check:** `gping --help` prints the usage and
the full option list — keep it; the chapters
ahead quote it rather than paraphrasing from
memory.
