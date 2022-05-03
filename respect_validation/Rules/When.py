from typing import Optional, Union

from respect_validation.Exceptions.AlwaysInvalidException import AlwaysInvalidException
from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.AlwaysInvalid import AlwaysInvalid


class When(AbstractRule):

    _when: AbstractRule
    _then: AbstractRule
    _else: Union[AbstractRule, AlwaysInvalid]

    def __init__(self, if_rule: AbstractRule, then_rule: AbstractRule, else_rule: Optional[AbstractRule] = None):
        super().__init__()
        self._when = if_rule
        self._then = then_rule
        if else_rule is None:
            else_rule = AlwaysInvalid()
            else_rule.set_template(AlwaysInvalidException.SIMPLE)

        self._else = else_rule

    def validate(self, input_val) -> bool:
        if self._when.validate(input_val):
            return self._then.validate(input_val)
        return self._else.validate(input_val)

    def claim(self, input_val) -> None:
        if self._when.validate(input_val):
            self._then.claim(input_val)
            return None
        self._else.claim(input_val)

    def check(self, input_val) -> None:
        if self._when.validate(input_val):
            self._then.check(input_val)
            return None
        self._else.check(input_val)
