from os.path import exists

from respect_validation.Rules.AbstractRule import AbstractRule


class Exists(AbstractRule):

    def validate(self, input_val):

        return isinstance(input_val, str) and exists(input_val)
