from os.path import islink

from respect_validation.Rules.AbstractRule import AbstractRule


class SymbolicLink(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str):
            return False

        return islink(input_val)
