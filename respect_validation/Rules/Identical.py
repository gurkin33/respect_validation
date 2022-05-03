from typing import Any

from respect_validation.Rules.AbstractRule import AbstractRule


class Identical(AbstractRule):

    _compare_to = None

    def __init__(self, compare_to: Any):
        super().__init__()
        self._compare_to = compare_to
        self.set_param('compare_to', compare_to)

    def validate(self, input_val):

        if type(self._compare_to) != type(input_val):
            return False
        return input_val == self._compare_to
