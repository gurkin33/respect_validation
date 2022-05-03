from typing import Optional, Any

from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractRelated(AbstractRule):

    _reference: Any
    _rule: Optional[AbstractRule] = None
    _mandatory: bool = True

    def __init__(self, reference: Any, rule: Optional[AbstractRule] = None, mandatory: bool = True):
        super().__init__()
        self._reference = reference
        self._rule = rule
        self._mandatory = mandatory

        if rule and rule.get_name() is not None:
            self.set_name(rule.get_name())
        elif isinstance(reference, str):
            self.set_name(reference)

    # base method for new rule
    def has_reference(self, input_val) -> bool:
        return False

    # base method for new rule
    def get_reference_value(self, input_val) -> bool:
        return False

    def get_reference(self):
        return self._reference

    def is_mandatory(self) -> bool:
        return self._mandatory

    def set_name(self, name) -> 'AbstractRelated':
        super().set_name(name)

        if isinstance(self._rule, AbstractRule):
            self._rule.set_name(name)

        return self

    def claim(self, input_val) -> None:
        has_reference = self.has_reference(input_val)
        if self._mandatory and not has_reference:
            raise self.report_error(input_val, {'has_reference': False})

        if self._rule is None or not has_reference:
            return

        try:
            self._rule.claim(self.get_reference_value(input_val))
        except ValidationException as e:
            nested_validation_exception = self.report_error(self._reference, {'has_reference': True})
            nested_validation_exception.add_child(e)  # type: ignore

            raise nested_validation_exception

    def check(self, input_val) -> None:
        has_reference = self.has_reference(input_val)
        if self._mandatory and not has_reference:
            raise self.report_error(input_val, {'has_reference': False})

        if self._rule is None or not has_reference:
            return

        self._rule.check(self.get_reference_value(input_val))

    def validate(self, input_val) -> bool:
        has_reference = self.has_reference(input_val)
        if self._mandatory and not has_reference:
            return False

        if self._rule is None or not has_reference:
            return True

        return self._rule.validate(self.get_reference_value(input_val))
