import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Cnpj(AbstractRule):

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        bases = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        digits = [int(d) for d in str(re.sub("[^0-9]", "", input_val))]

        if sum(digits) < 1:
            return False

        if len(digits) != 14:
            return False

        n = 0
        for i in range(12):
            n += digits[i] * bases[i+1]
        n = n % 11

        if digits[12] != (0 if n < 2 else 11 - n):
            return False

        n = 0
        for i in range(13):
            n += digits[i] * bases[i]
        n = n % 11

        check = 0 if n < 2 else 11 - n
        return digits[13] == check
