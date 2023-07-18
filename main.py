from address_book import AddressBook
from name import Name
from phone import Phone
from record import Record
from birthday import Birthday
from datetime import datetime

address_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError as e:
            return e

    return wrapper


@input_error
def add_command(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    birthday = Birthday(args[2]) if len(args) >= 3 else None
    rec = address_book.get(str(name))
    if rec:
        return rec.add_phone(phone)
    rec = Record(name, phone, birthday)
    address_book.add_record(rec)
    return f"Контакт {name}: {phone} успешно добавлен"


def change_command(*args):
    name = Name(args[0])
    old_phone = Phone(args[1])
    new_phone = Phone(args[2])
    rec = address_book.get(str(name))
    if rec:
        return rec.change_phone(old_phone, new_phone)
    return f"Контакт {name} не найден в адресной книге"


def days_to_birthday_command(*args):
    name = Name(args[0])
    rec = address_book.get(str(name))
    if rec and rec.birthday:
        days_left = rec.days_to_birthday()
        if days_left is not None:
            return f"До дня рождения {name} осталось {days_left} дней"
    return f"У контакта {name} нет дня рождения или он некорректен"


def exit_command(*args):
    address_book.save_to_file("data.json")  
    return "Bye"


def find_command(*args):
    search_text = " ".join(args)
    matching_contacts = address_book.find_contacts_by_text(search_text)
    if matching_contacts:
        return "\n".join(str(record) for record in matching_contacts)
    return f"Контактів зі збігом для '{search_text}' не знайдено"


def unknown_command(*args):
    pass


def show_all_command(*args):
    return address_book


COMMANDS = {
    add_command: ("add", "+"),
    change_command: ("change", "зміни"),
    days_to_birthday_command: ("days_to_birthday", "день рождения"),
    exit_command: ("bye", "exit", "end"),
    find_command: ("find", "search", "знайти"),  
    show_all_command: ("show all",),
}


def parser(text: str):
    for cmd, kwds in COMMANDS.items():
        for kwd in kwds:
            if text.lower().startswith(kwd):
                data = text[len(kwd):].strip().split()
                return cmd, data
    return unknown_command, []


def main():
    while True:
        user_input = input(">")

        cmd, data = parser(user_input)

        result = cmd(*data)

        print(result)

        if cmd == exit_command:
            break


if __name__ == "__main__":
    main()
