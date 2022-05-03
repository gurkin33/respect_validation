import re
from typing import Union, List, Any, Tuple

from respect_validation.Rules.AbstractRule import AbstractRule


class EndsWith(AbstractRule):

    _end_value = None

    def __init__(self, end_value: Union[str, List[Any], Tuple[Any]]):
        super().__init__()

        self._end_value = end_value

        self.set_param('end_value', end_value)

    def validate(self, input_val):
        return self._validate_equals(input_val)

    def _validate_equals(self, input_val):
        if isinstance(input_val, list) or isinstance(input_val, tuple):
            if len(input_val) == 0:
                return False
            return input_val[-1] == self._end_value

        if isinstance(input_val, str) and len(input_val) and input_val[-1] == self._end_value:
            return True

        return isinstance(self._end_value, str) and bool(re.match('.*'+self._end_value+'$', input_val))
