#!/bin/sh
# Fetch the fixture server's slow page (it waits 300 ms first).
exec curl -s -o /dev/null http://127.0.0.1:18091/slow
