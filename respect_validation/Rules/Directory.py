import os
from os.path import isdir

from respect_validation.Rules.AbstractRule import AbstractRule


class Directory(AbstractRule):

    def validate(self, input_val):

        if os.name == 'nt':
            return False

        if not isinstance(input_val, str):
            return False

        return isdir(input_val)
