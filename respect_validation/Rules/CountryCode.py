import pycountry

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class CountryCode(AbstractRule):
    ALPHA2 = 'alpha-2'
    ALPHA3 = 'alpha-3'
    NUMERIC = 'numeric'

    _set = None

    def __init__(self, code_set: str = 'alpha-2'):
        super().__init__()
        if code_set not in [self.NUMERIC, self.ALPHA2, self.ALPHA3]:
            raise ComponentException('{} is not a valid set for ISO 3166 (Available: {})'.format(
                code_set, [self.NUMERIC, self.ALPHA2, self.ALPHA3]))
        self._set = code_set

    def validate(self, input_val) -> bool:
        if self.ALPHA2 == self._set:
            return bool(pycountry.countries.get(alpha_2=str(input_val).upper()))
        if self.NUMERIC == self._set:
            return bool(pycountry.countries.get(numeric=str(input_val).upper()))
        return bool(pycountry.countries.get(alpha_3=str(input_val).upper()))
