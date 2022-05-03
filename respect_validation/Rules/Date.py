from datetime import datetime, date

from respect_validation.Exceptions import ComponentException
from respect_validation.Helpers.CanValidateDateTime import CanValidateDateTime
from respect_validation.Rules.AbstractRule import AbstractRule


class Date(AbstractRule, CanValidateDateTime):

    def __init__(self, date_format: str = '%Y-%m-%d'):
        super().__init__()
        if not self._is_date_format(date_format):
            raise ComponentException('"{}" is not a valid date format'.format(date_format))

        self._date_format = date_format
        self._sample = date.today().strftime(date_format)
        self.set_param('sample', str(self._sample))

    def validate(self, input_val):

        if isinstance(input_val, datetime):
            return True

        if not isinstance(input_val, str):
            return False

        return self._is_date_time(self._date_format, input_val)
