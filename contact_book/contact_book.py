"""Interactive command-line contact book with input validation.

Contacts are held in memory as a list of dictionaries. The menu lets the user
add, search, update, delete, list, and sort contacts, validating names, phone
numbers, and email addresses before storing them.
"""

from typing import Dict, List, Optional

from constants import (
    CONTACT_LINE,
    CONTACT_LIST_HEADER,
    CONTACT_NUMBER,
    Field,
    MENU_OPTIONS,
    MENU_TITLE,
    MSG_CONTACT_ADDED,
    MSG_CONTACT_DELETED,
    MSG_CONTACT_EXISTS,
    MSG_CONTACT_FOUND,
    MSG_CONTACT_NOT_FOUND,
    MSG_CONTACT_UPDATED,
    MSG_EMPTY_FIELD,
    MSG_EMPTY_QUERY,
    MSG_EXIT,
    MSG_INVALID_CHOICE,
    MSG_INVALID_EMAIL,
    MSG_INVALID_FIELD,
    MSG_INVALID_NAME,
    MSG_INVALID_PHONE,
    MSG_INVALID_SORT,
    MSG_NO_CONTACTS,
    MSG_NO_RESULTS,
    MSG_RESULT_COUNT,
    MSG_SKIP_FIELD,
    MSG_SORTED_BY,
    PROMPT_CHOICE,
    PROMPT_DELETE_NAME,
    PROMPT_EMAIL,
    PROMPT_NAME,
    PROMPT_NEW_FIELD,
    PROMPT_PARTIAL_NAME,
    PROMPT_PHONE,
    PROMPT_RETRY_FIELD,
    PROMPT_SEARCH_NAME,
    PROMPT_SORT_CHOICE,
    PROMPT_UPDATE_NAME,
    SORT_KEY_MAP,
    SORT_OPTIONS,
    SORT_TITLE,
)
from utils import is_valid_email, is_valid_name, is_valid_phone, safe_input

Contact = Dict[str, str]


class ContactBook:
    """Stores contacts and drives the interactive text menu."""

    VALID_FIELDS = {field.value for field in Field}
    FIELD_VALIDATORS = {
        Field.NAME.value: is_valid_name,
        Field.PHONE.value: is_valid_phone,
        Field.EMAIL.value: is_valid_email,
    }

    def __init__(self) -> None:
        self.contacts: List[Contact] = []

    def get_valid_name(self) -> str:
        while True:
            name = safe_input(PROMPT_NAME)
            if is_valid_name(name):
                return name
            print(MSG_INVALID_NAME)

    def get_valid_phone(self) -> str:
        while True:
            phone = safe_input(PROMPT_PHONE)
            if is_valid_phone(phone):
                return phone
            print(MSG_INVALID_PHONE)

    def get_valid_email(self) -> str:
        while True:
            email = safe_input(PROMPT_EMAIL)
            if is_valid_email(email):
                return email
            print(MSG_INVALID_EMAIL)

    def add_contact(self, name: str, phone: str, email: str) -> bool:
        if self.search_contact(name):
            return False

        self.contacts.append(
            {
                Field.NAME.value: name,
                Field.PHONE.value: phone,
                Field.EMAIL.value: email,
            }
        )
        return True

    def search_contact(self, name: str) -> Optional[Contact]:
        for contact in self.contacts:
            if contact[Field.NAME.value].lower() == name.lower():
                return contact
        return None

    def update_contact(self, name: str, updates: Contact) -> bool:
        contact = self.search_contact(name)

        if not contact:
            return False

        for field, value in updates.items():
            if field in self.VALID_FIELDS:
                contact[field] = value

        return True

    def delete_contact(self, name: str) -> bool:
        contact = self.search_contact(name)

        if not contact:
            return False

        self.contacts.remove(contact)
        return True

    def search_partial_name(self, query: str) -> List[Contact]:
        query = query.lower()
        return [
            contact
            for contact in self.contacts
            if query in contact[Field.NAME.value].lower()
        ]

    def sort_contacts(self, key: str) -> List[Contact]:
        return sorted(self.contacts, key=lambda contact: contact[key].lower())

    def print_contact_details(self, contact: Contact) -> None:
        for field in Field:
            label = field.value.capitalize()
            print(CONTACT_LINE.format(label=label, value=contact[field.value]))

    def display_contacts(self) -> None:
        if not self.contacts:
            print(MSG_NO_CONTACTS)
            return

        print(CONTACT_LIST_HEADER)
        for number, contact in enumerate(self.contacts, start=1):
            print(CONTACT_NUMBER.format(number=number))
            self.print_contact_details(contact)

    def collect_updates(self, contact: Contact) -> Contact:
        updates: Contact = {}
        for field in Field:
            key = field.value
            value = safe_input(PROMPT_NEW_FIELD.format(field=key, current=contact[key]))
            if not value:
                continue

            validator = self.FIELD_VALIDATORS[key]
            while not validator(value):
                print(MSG_INVALID_FIELD.format(field=key))
                value = safe_input(PROMPT_RETRY_FIELD.format(field=key))

            updates[key] = value

        return updates

    def handle_add(self) -> None:
        name = self.get_valid_name()
        phone = self.get_valid_phone()
        email = self.get_valid_email()

        if self.add_contact(name, phone, email):
            print(MSG_CONTACT_ADDED)
        else:
            print(MSG_CONTACT_EXISTS)

    def handle_search(self) -> None:
        name = safe_input(PROMPT_SEARCH_NAME)
        if not name:
            print(MSG_EMPTY_FIELD.format(field=Field.NAME.value.capitalize()))
            return

        contact = self.search_contact(name)
        if contact:
            print(MSG_CONTACT_FOUND)
            self.print_contact_details(contact)
        else:
            print(MSG_CONTACT_NOT_FOUND)

    def handle_update(self) -> None:
        name = safe_input(PROMPT_UPDATE_NAME)
        if not name:
            print(MSG_EMPTY_FIELD.format(field=Field.NAME.value.capitalize()))
            return

        contact = self.search_contact(name)
        if not contact:
            print(MSG_CONTACT_NOT_FOUND)
            return

        print(MSG_SKIP_FIELD)
        self.update_contact(name, self.collect_updates(contact))
        print(MSG_CONTACT_UPDATED)

    def handle_delete(self) -> None:
        name = safe_input(PROMPT_DELETE_NAME)
        if not name:
            print(MSG_EMPTY_FIELD.format(field=Field.NAME.value.capitalize()))
            return

        if self.delete_contact(name):
            print(MSG_CONTACT_DELETED)
        else:
            print(MSG_CONTACT_NOT_FOUND)

    def handle_partial_search(self) -> None:
        query = safe_input(PROMPT_PARTIAL_NAME)
        if not query:
            print(MSG_EMPTY_QUERY)
            return

        results = self.search_partial_name(query)
        if not results:
            print(MSG_NO_RESULTS)
            return

        print(MSG_RESULT_COUNT.format(count=len(results)))
        for contact in results:
            print()
            self.print_contact_details(contact)

    def handle_sort(self) -> None:
        print(SORT_TITLE)
        for option in SORT_OPTIONS:
            print(option)

        key = SORT_KEY_MAP.get(safe_input(PROMPT_SORT_CHOICE))
        if not key:
            print(MSG_INVALID_SORT)
            return

        print(MSG_SORTED_BY.format(field=key))
        for contact in self.sort_contacts(key):
            print()
            self.print_contact_details(contact)

    def display_menu(self) -> None:
        print(MENU_TITLE)
        for option in MENU_OPTIONS:
            print(option)

    def menu(self) -> None:
        while True:
            self.display_menu()
            choice = safe_input(PROMPT_CHOICE)

            match choice:
                case "1":
                    self.handle_add()
                case "2":
                    self.handle_search()
                case "3":
                    self.handle_update()
                case "4":
                    self.handle_delete()
                case "5":
                    self.display_contacts()
                case "6":
                    self.handle_partial_search()
                case "7":
                    self.handle_sort()
                case "8":
                    print(MSG_EXIT)
                    break
                case _:
                    print(MSG_INVALID_CHOICE)


def main() -> None:
    app = ContactBook()
    app.menu()


if __name__ == "__main__":
    main()
