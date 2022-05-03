from typing import List, Union

from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractWrapper import AbstractWrapper
from respect_validation.Rules.AllOf import AllOf
from respect_validation.Rules.Key import Key


class KeySet(AbstractWrapper):
    _keys: List[str]
    _key_rules: List[Key]

    def __init__(self, *keys: Key):

        self._key_rules = [self._get_key_rule(v) for v in keys]
        self._keys = [self._get_key_reference(k) for k in self._key_rules]

        super().__init__(AllOf(*self._key_rules))

        self.set_param('keys', self._keys)

    def claim(self, input_val) -> None:

        if not self._has_valid_structure(input_val):
            raise self.report_error(input_val) from None

        super().claim(input_val)

    def check(self, input_val) -> None:

        if not self._has_valid_structure(input_val):
            raise self.report_error(input_val) from None

        super().check(input_val)

    def validate(self, input_val) -> bool:

        if not self._has_valid_structure(input_val):
            return False

        return super().validate(input_val)

    def _get_key_rule(self, validatable: Union[Key, AllOf]) -> 'Key':
        if isinstance(validatable, Key):
            return validatable
        if not isinstance(validatable, AllOf) or len(validatable.get_rules()) != 1:
            raise ComponentException('KeySet rule accepts only Key rules') from None

        return self._get_key_rule(validatable.get_rules()[0])

    def _get_key_reference(self, rule: Key):
        return rule.get_reference()

    def _has_valid_structure(self, input_val) -> bool:

        if not isinstance(input_val, dict):
            return False

        temp_input = input_val.copy()

        for key_rule in self._key_rules:
            if key_rule.get_reference() not in temp_input.keys() and key_rule.is_mandatory():
                return False

            if key_rule.get_reference() in temp_input.keys():
                del temp_input[key_rule.get_reference()]

        return len(temp_input.keys()) == 0
