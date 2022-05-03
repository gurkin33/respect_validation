from respect_validation.Rules.AbstractRule import AbstractRule


class Even(AbstractRule):

    def validate(self, input_val):
        if not isinstance(input_val, int):
            return False

        return input_val % 2 == 0
