import math

from respect_validation.Rules.AbstractRule import AbstractRule


class Finite(AbstractRule):

    def validate(self, input_val):

        if isinstance(input_val, str) and input_val.isdigit():
            input_val = int(input_val)

        if isinstance(input_val, str):
            try:
                input_val = float(input_val)
            except Exception:
                return False

        if not isinstance(input_val, int) and not isinstance(input_val, float):
            return False

        return math.isfinite(input_val)
