from decimal import Decimal

from respect_validation.Rules.AbstractRule import AbstractRule


class Infinite(AbstractRule):

    def validate(self, input_val):

        try:
            test = Decimal(input_val)
        except Exception:
            return False

        return test.is_infinite()
