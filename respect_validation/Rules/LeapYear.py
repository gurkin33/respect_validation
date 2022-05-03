from datetime import datetime

from respect_validation.Helpers.CanValidateDateTime import CanValidateDateTime
from respect_validation.Rules.AbstractRule import AbstractRule


class LeapYear(AbstractRule, CanValidateDateTime):

    def validate(self, input_val):

        if isinstance(input_val, int) or isinstance(input_val, str):
            test_date = str(input_val) + '-02-29'
            return self._is_date_time("%Y-%m-%d", test_date)

        if isinstance(input_val, datetime):
            return input_val.strftime('%m-%d') == '02-29'

        return False
