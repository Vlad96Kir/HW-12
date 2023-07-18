from name import Name
from phone import Phone
from birthday import Birthday
from datetime import datetime

class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday

    def add_phone(self, phone: Phone):
        if phone.value not in [p.value for p in self.phones]:
            self.phones.append(phone)
            return f"Телефон {phone} добавлен для контакта {self.name}"
        return f"{phone} уже присутствует в телефонах контакта {self.name}"

    def change_phone(self, old_phone, new_phone):
        for idx, phone in enumerate(self.phones):
            if old_phone.value == phone.value:
                self.phones[idx] = new_phone
                return f"Старый телефон {old_phone} изменен на {new_phone} для контакта {self.name}"
        return f"Старый телефон {old_phone} не найден в телефонах контакта {self.name}"

    def __str__(self) -> str:
        return f"{self.name}: {', '.join(str(phone) for phone in self.phones)}"

    def days_to_birthday(self):
        if not self.birthday:
            return None

        today = datetime.now().date()
        birthday = self.birthday.to_datetime(today.year).date()

        if birthday < today:
            birthday = self.birthday.to_datetime(today.year + 1).date()

        days_left = (birthday - today).days
        return days_left
