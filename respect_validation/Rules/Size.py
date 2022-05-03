import re
from os.path import getsize
from typing import Optional, Union

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class Size(AbstractRule):

    _min_size = None
    _max_size = None
    _min_value = None
    _max_value = None

    def __init__(self, min_size: Optional[str] = None, max_size: Optional[str] = None):
        super().__init__()

        if min_size is not None and isinstance(min_size, str):
            self._min_size = min_size
            self._min_value = self._to_bytes(min_size)
        if max_size is not None and isinstance(max_size, str):
            self._max_size = max_size
            self._max_value = self._to_bytes(max_size)

        if self._min_value is None and self._max_value is None:
            raise ComponentException("Set correct file size, for example 1kb, 2mb, 3gb") from None

        if self._min_value and self._max_value and self._min_value > self._max_value:
            raise ComponentException("Minimum value must be less than or equals to maximum") from None

        self.set_param('min_size', min_size)
        self.set_param('max_size', max_size)
        self.set_param('max_value', self._max_value)
        self.set_param('min_value', self._min_value)

    def validate(self, input_val) -> bool:

        if isinstance(input_val, str):
            return self._is_valid_size(getsize(input_val))

        return False

    def _to_bytes(self, size: str) -> float:
        value: Union[float, None] = None
        units = ['b', 'kb', 'mb', 'gb', 'tb', 'pb', 'eb', 'zb', 'yb']

        for exponent in range(len(units)):
            probe = re.match(re.compile(r'^(\d+(.\d+)?)'+units[exponent]+'$', re.IGNORECASE), size)

            if not probe:
                continue
            value = float(probe.groups()[0]) * 1024 ** exponent

        if not isinstance(value, float):
            raise ComponentException('"{}" is not a recognized file size.'.format(size))

        return value

    def _is_valid_size(self, size: float) -> bool:

        if self._min_value is not None and self._max_value is not None:
            return self._min_value <= size <= self._max_value

        if self._min_value is not None:
            return size >= self._min_value

        if self._max_value is not None:
            return size <= self._max_value

        return False
