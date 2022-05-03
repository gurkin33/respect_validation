import re
from typing import Union, Pattern

from respect_validation.Rules.AbstractRule import AbstractRule


class Regex(AbstractRule):

    _regex: Union[str, Pattern[str]]

    def __init__(self, regex: Union[str, Pattern[str]]):
        super().__init__()
        self._regex = regex
        self.set_param('regex', regex)

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        return bool(re.match(self._regex, input_val))
