from respect_validation.Rules.AbstractRule import AbstractRule


class IntVal(AbstractRule):

    def validate(self, input_val):

        if isinstance(input_val, int):
            return True

        if isinstance(input_val, str) and input_val.isdigit():
            return True

        return False
