class Field:
    def __init__(self, value) -> None:
        self._value = value

    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return str(self)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
