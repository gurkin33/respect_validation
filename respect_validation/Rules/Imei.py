import re

from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.Luhn import Luhn


class Imei(AbstractRule):

    IMEI_SIZE = 15

    def validate(self, input_val):

        if isinstance(input_val, int):
            input_val = str(input_val)

        if not isinstance(input_val, str):
            return False

        numbers = str(re.sub(r'\D', '', input_val))

        if len(numbers) != self.IMEI_SIZE:
            return False

        return Luhn().validate(int(numbers))
