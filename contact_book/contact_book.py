from typing import Dict, List, Optional
import re


class ContactBook:
    """Contact Book using list of dictionaries with strict validation."""

    VALID_FIELDS = {"name", "phone", "email"}

    def __init__(self) -> None:
        self.contacts: List[Dict[str, str]] = []

    # -----------------------------
    # VALIDATION
    # -----------------------------
    def is_valid_name(self, name: str) -> bool:
        return bool(name.strip()) and all(part.isalpha() for part in name.split())

    def is_valid_phone(self, phone: str) -> bool:
        return phone.isdigit() and len(phone) == 11

    def is_valid_email(self, email: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, email))

    # -----------------------------
    # SAFE INPUT
    # -----------------------------
    def safe_input(self, prompt: str) -> str:
        try:
            return input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\nInput cancelled safely.")
            return ""

    # -----------------------------
    # BLOCKING VALID INPUT METHODS
    # -----------------------------
    def get_valid_name(self) -> str:
        while True:
            name = self.safe_input("Enter name: ")
            if self.is_valid_name(name):
                return name
            print(":x: Invalid name. Only alphabets allowed (e.g. Jamshaid Mehmood).")

    def get_valid_phone(self) -> str:
        while True:
            phone = self.safe_input("Enter phone (11 digits): ")
            if self.is_valid_phone(phone):
                return phone
            print(":x: Invalid phone. Must be exactly 11 digits.")

    def get_valid_email(self) -> str:
        while True:
            email = self.safe_input("Enter email: ")
            if self.is_valid_email(email):
                return email
            print(":x: Invalid email format (e.g. test@gmail.com).")

    # -----------------------------
    # CORE LOGIC
    # -----------------------------
    def add_contact(self, name: str, phone: str, email: str) -> bool:
        if self.search_contact(name):
            return False

        self.contacts.append(
            {"name": name, "phone": phone, "email": email}
        )
        return True

    def search_contact(self, name: str) -> Optional[Dict[str, str]]:
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                return contact
        return None

    def update_contact(self, name: str, updates: Dict[str, str]) -> bool:
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

    def display_contacts(self) -> None:
        if not self.contacts:
            print("\nNo contacts available.")
            return

        print("\n------ Contact List ------")

        for i, c in enumerate(self.contacts, start=1):
            print(f"\nContact {i}")
            print(f"Name : {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")

    def search_partial_name(self, query: str) -> List[Dict[str, str]]:
        """Search contacts by partial name (case-insensitive)."""
        results = []

        query = query.lower()

        for contact in self.contacts:
            if query in contact["name"].lower():
                results.append(contact)

        return results
    
    def sort_contacts(self, key: str) -> List[Dict[str, str]]:
        """Sort contacts by name, phone, or email."""
        if key not in self.VALID_FIELDS:
            return self.contacts

        return sorted(self.contacts, key=lambda x: x[key].lower())
    
    # -----------------------------
    # MENU
    # -----------------------------
    def menu(self) -> None:
        while True:
            print("\n====== CONTACT BOOK ======")
            print("1. Add Contact")
            print("2. Search Contact")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Display Contacts")
            print("6. Search by Partial Name")
            print("7. Sort Contacts")
            print("8. Exit")
            
            choice = self.safe_input("\nEnter your choice: ")

            # ---------------- ADD ----------------
            if choice == "1":
                name = self.get_valid_name()
                phone = self.get_valid_phone()
                email = self.get_valid_email()

                if self.add_contact(name, phone, email):
                    print("\nContact added successfully.")
                else:
                    print("\nContact already exists.")

            # ---------------- SEARCH ----------------
            elif choice == "2":
                name = self.safe_input("Enter name to search: ")

                if not name:
                    print("\nName cannot be empty.")
                    continue

                contact = self.search_contact(name)

                if contact:
                    print("\nContact Found")
                    print(f"Name : {contact['name']}")
                    print(f"Phone: {contact['phone']}")
                    print(f"Email: {contact['email']}")
                else:
                    print("\nContact not found.")

            # ---------------- UPDATE ----------------
            elif choice == "3":
                name = self.safe_input("Enter contact name: ")

                if not name:
                    print("\nName cannot be empty.")
                    continue

                contact = self.search_contact(name)

                if not contact:
                    print("\nContact not found.")
                    continue

                print("\nPress Enter to skip a field.\n")

                updates = {}

                new_name = self.safe_input(f"New name ({contact['name']}): ")
                if new_name:
                    while not self.is_valid_name(new_name):
                        print(":x: Invalid name.")
                        new_name = self.safe_input("Enter valid name: ")
                    updates["name"] = new_name

                new_phone = self.safe_input(f"New phone ({contact['phone']}): ")
                if new_phone:
                    while not self.is_valid_phone(new_phone):
                        print(":x: Invalid phone.")
                        new_phone = self.safe_input("Enter valid phone: ")
                    updates["phone"] = new_phone

                new_email = self.safe_input(f"New email ({contact['email']}): ")
                if new_email:
                    while not self.is_valid_email(new_email):
                        print(":x: Invalid email.")
                        new_email = self.safe_input("Enter valid email: ")
                    updates["email"] = new_email

                self.update_contact(name, updates)
                print("\nContact updated successfully.")

            # ---------------- DELETE ----------------
            elif choice == "4":
                name = self.safe_input("Enter contact name to delete: ")

                if not name:
                    print("\nName cannot be empty.")
                    continue

                if self.delete_contact(name):
                    print("\nContact deleted successfully.")
                else:
                    print("\nContact not found.")

            # ---------------- DISPLAY ----------------
            elif choice == "5":
                self.display_contacts()

            # ---------------- EXIT ----------------
            elif choice == "6":
                query = self.safe_input("Enter partial name: ")

                if not query:
                    print("\nSearch query cannot be empty.")
                    continue

                results = self.search_partial_name(query)

                if not results:
                    print("\nNo contacts found.")
                else:
                    print(f"\nFound {len(results)} result(s):")

                    for c in results:
                        print(f"\nName : {c['name']}")
                        print(f"Phone: {c['phone']}")
                        print(f"Email: {c['email']}")
            elif choice == "7":
                print("\nSort by:")
                print("1. Name")
                print("2. Phone")
                print("3. Email")

                option = self.safe_input("Enter choice: ")

                key_map = {
                    "1": "name",
                    "2": "phone",
                    "3": "email"
                }

                key = key_map.get(option)

                if not key:
                    print("\nInvalid sort option.")
                    continue

                sorted_contacts = self.sort_contacts(key)

                print(f"\nContacts sorted by {key}:")

                for c in sorted_contacts:
                    print(f"\nName : {c['name']}")
                    print(f"Phone: {c['phone']}")
                    print(f"Email: {c['email']}")
            elif choice == "8":
                print("\nThank you for using Contact Book!")
                break
            else:
                print("\nInvalid choice. Try again.")


def main() -> None:
    app = ContactBook()
    app.menu()


if __name__ == "__main__":
    main()
