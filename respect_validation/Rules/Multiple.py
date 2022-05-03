from respect_validation.Rules.AbstractRule import AbstractRule


class Multiple(AbstractRule):

    _multiple_of = None

    def __init__(self, multiple_of: int):
        super().__init__()

        self._multiple_of = multiple_of
        self.set_param('multiple_of', multiple_of)

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, int) and not str(input_val).isdigit():
            return False

        if input_val == 0 and self._multiple_of == 0:
            return True

        if self._multiple_of == 0:
            return False

        return bool(input_val % self._multiple_of == 0)
