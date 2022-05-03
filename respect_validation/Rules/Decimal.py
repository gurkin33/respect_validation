from respect_validation.Rules.AbstractRule import AbstractRule


class Decimal(AbstractRule):

    def __init__(self, decimals: int):
        super().__init__()
        self._decimal = int(decimals)
        self.set_param('decimals', decimals)

    def validate(self, input_val):

        if isinstance(input_val, int) and type(input_val).__name__ != 'bool':
            return self._decimal == 0

        if isinstance(input_val, str) and '.' in input_val:
            try:
                float(input_val)
                return len(input_val.split('.')[1]) == self._decimal
            except Exception:
                return False

        if isinstance(input_val, float):
            return len(str(input_val).split('.')[1]) == self._decimal

        return False
