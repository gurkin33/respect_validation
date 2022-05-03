from respect_validation.Rules.AbstractRule import AbstractRule


class AlwaysInvalid(AbstractRule):

    def validate(self, input_val):
        return False
