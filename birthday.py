from field import Field
from datetime import datetime

class Birthday(Field):
    def __init__(self, value=None) -> None:
        super().__init__(value)
        self.value = value  # Виконуємо валідацію за допомогою сеттера

    @Field.value.setter
    def value(self, new_value):
        if new_value is not None and not self.validate_birthday(new_value):
            raise ValueError("Invalid birthday format")
        self._value = new_value

    def validate_birthday(self, birthday):
        if not birthday:
            return True

        # Перевірка, чи дата народження має правильний формат 'YYYY-MM-DD'
        try:
            datetime.strptime(birthday, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def to_datetime(self, year):
        if not self.value:
            return None

        # Перетворюємо рядок дати народження в об'єкт datetime
        return datetime.strptime(self.value, "%Y-%m-%d").replace(year=year)
