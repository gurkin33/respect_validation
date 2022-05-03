import re

from respect_validation.Rules.AbstractRule import AbstractRule


class PolishIdCard(AbstractRule):

    ASCII_CODE_0 = 48
    ASCII_CODE_7 = 55
    ASCII_CODE_9 = 57
    ASCII_CODE_A = 65

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str) or not re.match(r'^[A-Z0-9]{9}$', input_val):
            return False

        weights = [7, 3, 1, 0, 7, 3, 1, 7, 3]
        weighted_sum = 0

        for i in range(9):
            code = ord(input_val[i])
            if i < 3 and code <= self.ASCII_CODE_9:
                return False
            if i > 2 and code >= self.ASCII_CODE_A:
                return False

            difference = self.ASCII_CODE_0 if code <= self.ASCII_CODE_9 else self.ASCII_CODE_7

            weighted_sum += (code - difference) * weights[i]

        return int(weighted_sum % 10) == int(input_val[3])
