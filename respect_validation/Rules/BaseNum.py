import re
from typing import Optional

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class BaseNum(AbstractRule):

    chars = ''
    base: int

    def __init__(self, base: int, chars: Optional[str] = None):
        super().__init__()
        if chars is None:
            self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        else:
            self.chars = chars

        maximum = len(self.chars)
        if base is None or not isinstance(base, int):
            raise ComponentException('a base must be integer between 1 and {}'.format(maximum))
        if base > maximum:
            raise ComponentException('a base between 1 and {} is required'.format(maximum))

        self.base = base
        self.set_param('base', base)

    def validate(self, input_val) -> bool:
        valid = r"^[" + self.chars[:self.base] + "]+$"

        return bool(re.search(valid, input_val))
