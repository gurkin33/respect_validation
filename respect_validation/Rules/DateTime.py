from datetime import datetime, date
from typing import Optional

from respect_validation.Exceptions import ComponentException
from respect_validation.Helpers.CanValidateDateTime import CanValidateDateTime
from respect_validation.Rules.AbstractRule import AbstractRule


class DateTime(AbstractRule, CanValidateDateTime):

    def __init__(self, date_format: Optional[str] = None):
        super().__init__()

        self._date_format = date_format
        if date_format:
            if not self._is_date_format(date_format):
                raise ComponentException('"{}" is not a valid date format'.format(date_format))
            self._sample = date.today().strftime(date_format)
            self.set_param('sample', str(self._sample))
            self.set_param('format', date_format)

    def validate(self, input_val):

        if isinstance(input_val, datetime):
            return True

        if isinstance(input_val, str) and self._is_iso_format(input_val):
            return True

        if not isinstance(input_val, str) or self._date_format is None:
            return False

        return self._is_date_time(self._date_format, input_val)
