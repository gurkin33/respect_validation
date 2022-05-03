from respect_validation.Rules.AbstractRule import AbstractRule


class Countable(AbstractRule):

    def validate(self, input_val):
        return hasattr(input_val, '__len__')
