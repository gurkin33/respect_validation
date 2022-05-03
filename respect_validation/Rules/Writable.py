import os

from respect_validation.Rules.AbstractRule import AbstractRule


class Writable(AbstractRule):

    def validate(self, input_val) -> bool:

        if os.name == 'nt':
            return False

        return isinstance(input_val, str) and os.access(input_val, os.W_OK)
