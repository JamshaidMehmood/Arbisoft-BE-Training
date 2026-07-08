"""Field definitions, validation patterns, and user-facing text for the contact book.

Keeping every literal in one place means a label, prompt, or rule is changed
in a single spot instead of being hunted down across the application.
"""

from enum import Enum


class Field(str, Enum):
    """Names of the fields stored for every contact."""

    NAME = "name"
    PHONE = "phone"
    EMAIL = "email"


PHONE_LENGTH = 11

NAME_REGEX = r"^[A-Za-z]+(?:[ '-][A-Za-z]+)*$"
EMAIL_REGEX = r"^[\w.-]+@[\w.-]+\.\w+$"

MENU_TITLE = "\n====== CONTACT BOOK ======"
MENU_OPTIONS = (
    "1. Add Contact",
    "2. Search Contact",
    "3. Update Contact",
    "4. Delete Contact",
    "5. Display Contacts",
    "6. Search by Partial Name",
    "7. Sort Contacts",
    "8. Exit",
)

SORT_TITLE = "\nSort by:"
SORT_OPTIONS = (
    "1. Name",
    "2. Phone",
    "3. Email",
)
SORT_KEY_MAP = {
    "1": Field.NAME.value,
    "2": Field.PHONE.value,
    "3": Field.EMAIL.value,
}

PROMPT_CHOICE = "\nEnter your choice: "
PROMPT_NAME = "Enter name: "
PROMPT_PHONE = f"Enter phone ({PHONE_LENGTH} digits): "
PROMPT_EMAIL = "Enter email: "
PROMPT_SEARCH_NAME = "Enter name to search: "
PROMPT_UPDATE_NAME = "Enter contact name: "
PROMPT_DELETE_NAME = "Enter contact name to delete: "
PROMPT_PARTIAL_NAME = "Enter partial name: "
PROMPT_SORT_CHOICE = "Enter choice: "
PROMPT_NEW_FIELD = "New {field} ({current}): "
PROMPT_RETRY_FIELD = "Enter valid {field}: "

CONTACT_LINE = "{label:<5}: {value}"
CONTACT_LIST_HEADER = "\n------ Contact List ------"
CONTACT_NUMBER = "\nContact {number}"

MSG_INPUT_CANCELLED = "\n\nInput cancelled safely."
MSG_INVALID_NAME = (
    "Error: Invalid name. Letters, spaces, hyphens, and apostrophes only "
    "(e.g. Jamshaid Mehmood)."
)
MSG_INVALID_PHONE = f"Error: Invalid phone. Must be exactly {PHONE_LENGTH} digits."
MSG_INVALID_EMAIL = "Error: Invalid email format (e.g. test@gmail.com)."
MSG_INVALID_FIELD = "Error: Invalid {field}."
MSG_EMPTY_FIELD = "\n{field} cannot be empty."
MSG_CONTACT_ADDED = "\nContact added successfully."
MSG_CONTACT_EXISTS = "\nContact already exists."
MSG_CONTACT_FOUND = "\nContact Found"
MSG_CONTACT_NOT_FOUND = "\nContact not found."
MSG_CONTACT_UPDATED = "\nContact updated successfully."
MSG_CONTACT_DELETED = "\nContact deleted successfully."
MSG_NO_CONTACTS = "\nNo contacts available."
MSG_SKIP_FIELD = "\nPress Enter to skip a field.\n"
MSG_EMPTY_QUERY = "\nSearch query cannot be empty."
MSG_NO_RESULTS = "\nNo contacts found."
MSG_RESULT_COUNT = "\nFound {count} result(s):"
MSG_SORTED_BY = "\nContacts sorted by {field}:"
MSG_INVALID_SORT = "\nInvalid sort option."
MSG_INVALID_CHOICE = "\nInvalid choice. Try again."
MSG_EXIT = "\nThank you for using Contact Book!"
