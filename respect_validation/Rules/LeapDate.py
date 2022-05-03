from datetime import datetime

from respect_validation.Exceptions import ComponentException
from respect_validation.Helpers.CanValidateDateTime import CanValidateDateTime
from respect_validation.Rules.AbstractRule import AbstractRule


class LeapDate(AbstractRule, CanValidateDateTime):

    _date_format: str

    def __init__(self, date_format: str = "%Y-%m-%d"):
        super().__init__()
        self._date_format = date_format
        if not self._is_date_format(date_format):
            raise ComponentException('"{}" is not a valid date format'.format(date_format))

    def validate(self, input_val):
        if isinstance(input_val, datetime):
            return input_val.strftime('%m-%d') == '02-29'

        if not isinstance(input_val, str) or self._date_format is None:
            return False

        try:
            datetime.strptime(input_val, self._date_format)
        except Exception:
            return False

        if not self._is_date_time(self._date_format, input_val):
            return False

        return str(datetime.strptime(input_val, self._date_format).strftime('%m-%d')) == '02-29'
