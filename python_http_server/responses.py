"""Response helper methods."""

from .constants import CONTENT_TYPE_JSON, CONTENT_TYPE_TEXT


def send_response(handler, status_code, body, content_type):
    """Send HTTP response"""
    handler.send_response(status_code)
    handler.send_header("Content-Type", content_type)
    handler.end_headers()

    if isinstance(body, str):
        body = body.encode()

    handler.wfile.write(body)


def send_text(handler, status_code, message):
    send_response(handler, status_code, message, CONTENT_TYPE_TEXT)


def send_json(handler, status_code, payload):
    send_response(handler, status_code, payload, CONTENT_TYPE_JSON)
