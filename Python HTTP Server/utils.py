"""Utility helpers."""

from datetime import datetime

from constants import TIME_FORMAT


def get_current_time() -> str:
    """Return current server time."""
    return datetime.now().strftime(TIME_FORMAT)


def build_json(key: str, value: str) -> str:
    """Build JSON manually."""
    return f'{{"{key}":"{value}"}}'
