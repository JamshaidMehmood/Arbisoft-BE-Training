"""Utility helpers."""

import json
from datetime import datetime

from .constants import TIME_FORMAT


def get_current_time() -> str:
    return datetime.now().strftime(TIME_FORMAT)


def build_json(key: str, value: str) -> str:
    return json.dumps({key: value})
