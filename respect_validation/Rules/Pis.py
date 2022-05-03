import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Pis(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, int):
            input_val = str(input_val)

        if not isinstance(input_val, str):
            return False

        digits = str(re.sub(r'\D', '', input_val))

        if len(digits) != 11 or bool(re.search(re.compile(r'^'+digits[0]+'{11}$'), digits)):
            return False

        multipliers = [3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        summation = 0

        for position in range(10):
            summation += int(digits[position]) * multipliers[position]

        check_digit = int(digits[10])

        modulo = summation % 11

        return check_digit == (0 if modulo < 2 else 11 - modulo)
