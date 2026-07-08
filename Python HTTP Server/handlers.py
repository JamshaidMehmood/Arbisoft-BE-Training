"""HTTP request handlers."""

from http.server import BaseHTTPRequestHandler

from constants import (
    ROOT_PATH,
    TIME_PATH,
    ECHO_PATH,
    STATUS_OK,
    STATUS_NOT_FOUND,
    STATUS_METHOD_NOT_ALLOWED,
    WELCOME_MESSAGE,
    NOT_FOUND_MESSAGE,
    METHOD_NOT_ALLOWED_MESSAGE,
)

from responses import (
    send_json,
    send_text,
)

from utils import (
    build_json,
    get_current_time,
)


class RequestHandler(BaseHTTPRequestHandler):
    """Handles incoming HTTP requests."""

    def do_GET(self):
        """Handle GET requests."""

        if self.path == ROOT_PATH:
            send_text(
                self,
                STATUS_OK,
                WELCOME_MESSAGE,
            )
            return

        if self.path == TIME_PATH:
            payload = build_json(
                "server_time",
                get_current_time(),
            )

            send_json(
                self,
                STATUS_OK,
                payload,
            )
            return

        send_text(
            self,
            STATUS_NOT_FOUND,
            NOT_FOUND_MESSAGE,
        )

    def do_POST(self):
        """Handle POST requests."""

        if self.path != ECHO_PATH:
            send_text(
                self,
                STATUS_NOT_FOUND,
                NOT_FOUND_MESSAGE,
            )
            return

        content_length = int(
            self.headers.get("Content-Length", 0)
        )

        body = self.rfile.read(content_length)

        send_text(
            self,
            STATUS_OK,
            body,
        )

    def do_PUT(self):
        self.method_not_allowed()

    def do_DELETE(self):
        self.method_not_allowed()

    def method_not_allowed(self):
        """Return 405 response."""

        send_text(
            self,
            STATUS_METHOD_NOT_ALLOWED,
            METHOD_NOT_ALLOWED_MESSAGE,
        )

    def log_message(self, *_):
        """Disable default console logging."""
        return
