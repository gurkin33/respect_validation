import phonenumbers

from respect_validation.Rules.AbstractRule import AbstractRule


class Phone(AbstractRule):

    _strict: bool

    def __init__(self, strict: bool = False):
        super().__init__()
        self._strict = strict

    def validate(self, input_val) -> bool:
        if not isinstance(input_val, str):
            return False

        if self._strict:
            try:
                return bool(phonenumbers.is_valid_number(phonenumbers.parse(input_val)))
            except Exception:
                return False
        try:
            return bool(phonenumbers.is_possible_number(phonenumbers.parse(input_val)))
        except Exception:
            return False
