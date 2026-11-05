#!/bin/sh
# Fetch the fixture server's fast page and say nothing.
exec curl -s -o /dev/null http://127.0.0.1:18091/fast
