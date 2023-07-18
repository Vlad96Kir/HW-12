from field import Field

class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)
        self.value = value  # Перевірка на коректність проводиться за допомогою сеттера

    @Field.value.setter
    def value(self, new_value):
        if not self.validate_phone(new_value):
            raise ValueError("Неверный формат номера телефона")
        self._value = new_value

    @staticmethod
    def validate_phone(phone):
        # Тут можна додати регулярний вираз для перевірки коректності формату номера телефону
        # Наприклад, можна перевірити, чи номер складається лише з цифр та може мати певну довжину.
        # У цьому прикладі ми просто перевіряємо, чи номер не порожній.
        return bool(phone)
