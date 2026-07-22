"""HTTP server configuration."""

from http.server import HTTPServer

from .constants import HOST, PORT
from .handlers import RequestHandler


class HttpServer:
    """Creates and runs the HTTP server."""

    def __init__(self):
        self.server = HTTPServer((HOST, PORT), RequestHandler)

    def run(self):
        """Start serving requests"""
        print(f"Server running at http://{HOST}:{PORT}")
        self.server.serve_forever()
