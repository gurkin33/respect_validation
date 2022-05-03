import math

from respect_validation.Rules.AbstractRule import AbstractRule


class PerfectSquare(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, str) and input_val.isdigit():
            input_val = int(input_val)

        if not isinstance(input_val, int) or input_val < 0:
            return False

        return math.sqrt(input_val) == math.floor(math.sqrt(input_val))
