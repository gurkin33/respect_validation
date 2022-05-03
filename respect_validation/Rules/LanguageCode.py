import pycountry

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRule import AbstractRule


class LanguageCode(AbstractRule):
    ALPHA2 = 'alpha-2'
    ALPHA3 = 'alpha-3'

    AVAILABLE_SETS = ['alpha-2', 'alpha-3']

    def __init__(self, code_set: str = 'alpha-2'):
        super().__init__()
        if code_set not in [self.ALPHA2, self.ALPHA3]:
            raise ComponentException('{} is not a valid set for ISO 639-3 (Available: {})'.format(
                code_set, [self.ALPHA2, self.ALPHA3]))
        self._set = code_set
        self.set_param('code_set', code_set)

    def validate(self, input_val) -> bool:
        if self.ALPHA2 == self._set:
            return bool(pycountry.languages.get(alpha_2=str(input_val).upper()))
        return bool(pycountry.languages.get(alpha_3=str(input_val).upper()))
