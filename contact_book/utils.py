"""Generic validation and input helpers shared across the contact book.

These functions carry no contact-book state, so they live here rather than on
the ``ContactBook`` class and can be reused by any module that needs them.
"""

import re

from constants import EMAIL_REGEX, MSG_INPUT_CANCELLED, NAME_REGEX, PHONE_LENGTH


def is_valid_name(name: str) -> bool:
    return bool(re.match(NAME_REGEX, name.strip()))


def is_valid_phone(phone: str) -> bool:
    return phone.isdigit() and len(phone) == PHONE_LENGTH


def is_valid_email(email: str) -> bool:
    return bool(re.match(EMAIL_REGEX, email))


def safe_input(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        print(MSG_INPUT_CANCELLED)
        return ""
