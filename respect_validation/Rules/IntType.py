from respect_validation.Rules.AbstractRule import AbstractRule


class IntType(AbstractRule):

    def validate(self, input_val):
        return isinstance(input_val, int)
