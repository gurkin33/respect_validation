from os.path import isfile

from respect_validation.Rules.AbstractRule import AbstractRule


class File(AbstractRule):

    def validate(self, input_val):

        return isinstance(input_val, str) and isfile(input_val)
