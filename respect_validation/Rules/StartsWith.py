from typing import Any

from respect_validation.Rules.AbstractRule import AbstractRule


class StartsWith(AbstractRule):

    _start_value: Any

    def __init__(self, start_value: Any):
        super().__init__()

        self._start_value = start_value

        self.set_param('start_value', start_value)

    def validate(self, input_val):
        return self._validate_equals(input_val)

    def _validate_equals(self, input_val):
        if isinstance(input_val, list) or isinstance(input_val, tuple):
            if len(input_val) == 0:
                return False
            return input_val[0] == self._start_value

        return isinstance(input_val, str) and input_val.find(self._start_value) == 0
