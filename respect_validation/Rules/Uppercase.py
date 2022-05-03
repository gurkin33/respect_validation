from respect_validation.Rules.AbstractRule import AbstractRule


class Uppercase(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str):
            return False

        return input_val == input_val.upper()
