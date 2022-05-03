from respect_validation.Rules.AbstractRule import AbstractRule


class Lowercase(AbstractRule):

    def validate(self, input_val):
        if not isinstance(input_val, str):
            return False

        return input_val.islower()
