import pycountry

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class CurrencyCode(AbstractRule):

    ALPHA3 = 'alpha-3'
    NUMERIC = 'numeric'

    def __init__(self, code_set: str = 'alpha-3'):
        super().__init__()
        if code_set not in [self.NUMERIC, self.ALPHA3]:
            raise ComponentException('{} is not a valid set for ISO 4217 (Available: {}, {})'.format(
                code_set, self.NUMERIC, self.ALPHA3))
        self._set = code_set

    def validate(self, input_val) -> bool:
        if self.NUMERIC == self._set:
            return bool(pycountry.currencies.get(numeric=str(input_val).upper()))
        return bool(pycountry.currencies.get(alpha_3=str(input_val).upper()))
