#!/usr/bin/env python3
"""A tiny web server on 127.0.0.1:18091 with two personalities.

/fast answers at once. /slow waits 300 ms before answering, like a
server doing real work (or struggling). Anything else gets a 404.

Run it in one terminal, fetch from it in another, then stop it with
Ctrl-C. It only ever talks to this machine.
"""
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path == "/slow":
            time.sleep(0.30)
        elif self.path != "/fast":
            self.send_response(404)
            self.end_headers()
            return
        body = b"fixture server\n"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, *args) -> None:  # keep the terminal quiet
        pass


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 18091), Handler)
    print("listening on 127.0.0.1:18091 — /fast and /slow")
    server.serve_forever()
