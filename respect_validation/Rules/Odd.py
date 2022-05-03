from respect_validation.Rules.AbstractRule import AbstractRule


class Odd(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, str) and input_val.isdigit():
            input_val = int(input_val)

        if not isinstance(input_val, int):
            return False

        return input_val % 2 != 0
