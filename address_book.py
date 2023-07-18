import json
from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"

    def save_to_file(self, file_path):
        with open(file_path, "w") as file:
            data = {
                "contacts": [record.serialize() for record in self.data.values()]
            }
            json.dump(data, file, indent=2)

    def load_from_file(self, file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
            for contact_data in data["contacts"]:
                record = Record.deserialize(contact_data)
                self.add_record(record)

    def find_contacts_by_text(self, search_text):
        matching_contacts = []
        for contact in self.data.values():
            if search_text.lower() in contact.name.value.lower():
                matching_contacts.append(contact)
            for phone in contact.phones:
                if search_text in phone.value:
                    matching_contacts.append(contact)
        return matching_contacts

    def __str__(self) -> str:
        return "\n".join(str(r) for r in self.data.values())

    def __iter__(self):
        self._iter_index = 0
        return self

    def __next__(self):
        if self._iter_index >= len(self.data):
            raise StopIteration
        items_per_page = 3  # Adjust this number based on how many items you want per page
        page_items = list(self.data.values())[self._iter_index:self._iter_index + items_per_page]
        self._iter_index += items_per_page
        return "\n".join(str(item) for item in page_items)
