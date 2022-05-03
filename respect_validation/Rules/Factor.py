from respect_validation.Rules.AbstractRule import AbstractRule


class Factor(AbstractRule):

    _dividend: int

    def __init__(self, dividend: int):
        super().__init__()
        self._dividend = dividend
        self.set_param('dividend', dividend)

    def validate(self, input_val):

        #  Every integer is a factor of zero, and zero is the only integer that
        #  has zero for a factor.
        if self._dividend == 0:
            return True
        #  Factors must be integers that are not zero.
        if input_val == 0 or (not isinstance(input_val, int) and not isinstance(input_val, float)):
            return False

        input_val = abs(input_val)
        dividend = abs(self._dividend)
        if input_val == 0 or 1 > input_val > 0:
            return False

        #  The dividend divided by the input must be an integer if input is a
        #  factor of the dividend.
        return dividend % input_val == 0
