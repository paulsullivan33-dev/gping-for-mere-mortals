#!/usr/bin/env python3
"""A listener that opens its door and then never answers it.

It binds 127.0.0.1:18091 and calls listen() with a backlog of one,
then sleeps forever without ever calling accept(). The first
connection or two complete from the kernel's queue; after that,
connection attempts are left hanging — a homemade picture of a
server that has stopped coping. Ctrl-C to stop it.
"""
import socket
import time

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("127.0.0.1", 18091))
sock.listen(1)
print("listening on 127.0.0.1:18091 but never accepting")
while True:
    time.sleep(3600)
