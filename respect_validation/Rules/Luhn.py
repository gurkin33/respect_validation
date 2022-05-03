import re

from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.Digit import Digit


class Luhn(AbstractRule):

    def validate(self, input_val):
        if not Digit().validate(input_val):
            return False

        return self._is_valid(str(input_val))

    def _is_valid(self, input_val: str):
        _sum = 0
        digits = [int(d) for d in str(re.sub("[^0-9]", "", input_val))]
        num_digits = len(digits)
        parity = num_digits % 2
        for i in range(num_digits):
            digit = digits[i]
            if parity == i % 2:
                digit = digit << 1
                if 9 < digit:
                    digit -= 9
            _sum += digit

        return _sum % 10 == 0
