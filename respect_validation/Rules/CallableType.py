from respect_validation.Rules.AbstractRule import AbstractRule


class CallableType(AbstractRule):

    def validate(self, input_val):
        return callable(input_val)
