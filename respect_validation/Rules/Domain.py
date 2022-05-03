from typing import List, Any

from respect_validation.Exceptions import NestedValidationException, ValidationException
from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.AllOf import AllOf
from respect_validation.Rules.Alnum import Alnum
from respect_validation.Rules.AnyOf import AnyOf
from respect_validation.Rules.Callback import Callback
from respect_validation.Rules.Contains import Contains
from respect_validation.Rules.EndsWith import EndsWith
from respect_validation.Rules.Length import Length
from respect_validation.Rules.NoWhitespace import NoWhitespace
from respect_validation.Rules.Not import Not
from respect_validation.Rules.StartsWith import StartsWith
from respect_validation.Rules.StringType import StringType
from respect_validation.Rules.Tld import Tld


class Domain(AbstractRule):

    _generic_rule = None
    _tld_rule = None
    _parts_rule = None

    def __init__(self, tld_check: bool = True):
        super().__init__()
        self._tld_rule = self._create_tld_rule(tld_check)
        self._generic_rule = self._create_generic_rule()
        self._parts_rule = self._create_parts_rule()

    def claim(self, input_val: str):

        exceptions: List[Any] = []

        self.get_claim_exception(exceptions, self._generic_rule, input_val)
        self._raise_exceptions(exceptions, input_val)

        parts = input_val.split('.')
        if len(parts) >= 2:
            self.get_claim_exception(exceptions, self._tld_rule, parts.pop())

        for part in parts:
            self.get_claim_exception(exceptions, self._parts_rule, part)

        self._raise_exceptions(exceptions, input_val)

    def validate(self, input_val: str):
        try:
            self.claim(input_val)
        except ValidationException:
            return False
        return True

    def check(self, input_val: str):
        try:
            self.claim(input_val)
        except NestedValidationException as nv:
            # for exception in nv.get_children():
            #     raise exception
            raise nv

    def get_claim_exception(self, exceptions: List[Any], rule, input_val):
        try:
            rule.claim(input_val)
        except NestedValidationException as nv:
            exceptions += nv.get_children()
        except ValidationException as ve:
            exceptions.append(ve)

    def _create_generic_rule(self):
        return AllOf(
            StringType(),
            NoWhitespace(),
            Contains('.'),
            Length(3)
        )

    def _create_tld_rule(self, tld_check: bool):

        if tld_check:
            return Tld()

        return AllOf(
            Not(StartsWith('-')),
            NoWhitespace(),
            Length(2)
        )

    def _create_parts_rule(self):

        return AllOf(
            Alnum('-'),
            Not(StartsWith('-')),
            AnyOf(
                Not(Contains('--')),
                Callback(self._check_dashes)
            ),
            Not(EndsWith('-'))
        )

    def _check_dashes(self, input_val):
        return input_val.count('--') == 1

    def _raise_exceptions(self, exceptions, input_val):
        if len(exceptions):
            domain_exception = self.report_error(input_val)
            domain_exception.add_children(exceptions)  # type: ignore
            raise domain_exception
