import os

from respect_validation.Rules.AbstractRule import AbstractRule


class Executable(AbstractRule):

    def validate(self, input_val):

        if os.name == 'nt':
            return False

        if not isinstance(input_val, str):
            return False

        return os.access(input_val, os.X_OK)
