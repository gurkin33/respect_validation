from respect_validation.Rules.AbstractRule import AbstractRule


class FloatType(AbstractRule):

    def validate(self, input_val):

        return isinstance(input_val, float)
