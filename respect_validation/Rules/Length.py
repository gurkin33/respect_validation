from typing import Optional

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Length(AbstractRule):

    _min_value = None
    _max_value = None
    _inclusive = None

    def __init__(self, min_value: Optional[int] = None, max_value: Optional[int] = None, inclusive: bool = True):
        super().__init__()
        self._min_value = min_value
        self._max_value = max_value
        self._inclusive = inclusive

        if max_value is not None and min_value is not None and min_value > max_value:
            raise ComponentException("{} cannot be less than {} for validation".format(max_value, min_value))

        self.set_param('min_value', min_value)
        self.set_param('max_value', max_value)
        self.set_param('inclusive', inclusive)

    def validate(self, input_val) -> bool:
        length = self._extract_lenght(input_val)

        if length is None:
            return False

        return self._validate_min(length) and self._validate_max(length)

    def _extract_lenght(self, input_val):

        if hasattr(input_val, '__len__'):
            return len(input_val)

        if hasattr(input_val, '__str__'):
            return len(str(input_val))

        return None

    def _validate_min(self, length) -> bool:

        if self._min_value is None:
            return True

        if self._inclusive:
            return bool(length >= self._min_value)

        return bool(length > self._min_value)

    def _validate_max(self, length) -> bool:
        if self._max_value is None:
            return True

        if self._inclusive:
            return bool(length <= self._max_value)

        return bool(length < self._max_value)
