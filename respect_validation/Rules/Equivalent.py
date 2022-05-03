from typing import Any

from respect_validation.Rules.AbstractRule import AbstractRule


class Equivalent(AbstractRule):

    _compare_to = None

    def __init__(self, compare_to: Any):
        super().__init__()
        self._compare_to = compare_to
        self.set_param('compare_to', compare_to)

    def validate(self, input_val):
        if isinstance(input_val, str):
            if not isinstance(self._compare_to, str):
                return False
            return input_val.upper() == self._compare_to.upper()

        return input_val == self._compare_to
