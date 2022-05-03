from typing import List, Callable, Any, Dict

from respect_validation.Exceptions.NestedValidationException import NestedValidationException
from respect_validation.Exceptions.ValidationException import ValidationException
from respect_validation.Factory import Factory
from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractComposite(AbstractRule):

    _rules: List[Any] = []

    def __init__(self, *rules: Any):
        super().__init__()
        self._rules = list(rules)

    def add_rule(self, rule) -> 'AbstractComposite':
        if self.should_name_overwritten(rule) and self.get_name() is not None:
            rule.set_name(self.get_name())

        self._rules.append(rule)
        return self

    def get_rules(self) -> List[Any]:
        return self._rules

    def get_claim_exception(self, input_val) -> List[ValidationException]:
        return list(filter(None, map(self.raised_rules(input_val), self.get_rules())))

    def report_error(self, input_val, extra_params: Dict[str, Any] = {}) -> Any:
        return Factory.get_default_instance().exception(self, input_val, extra_params)

    def set_name(self, name: str) -> 'AbstractRule':
        parent_name = self.get_name()
        for rule in self.get_rules():
            rule_name = rule.get_name()
            if rule_name and parent_name != rule_name:
                continue
            rule.set_name(name)
        return super().set_name(name)

    # def update_exception_template(self, exception) -> None:
    #     if self._template is None or exception.has_custome_template():
    #         return
    #
    #     exception.update_template(self._template)

    def raised_rules(self, input_val) -> Callable[[AbstractRule], None]:
        def raised_rules_helper(rule: AbstractRule):
            try:
                rule.claim(input_val)
            except NestedValidationException as nve:
                self.update_exception_template(nve)
                return nve
            except ValidationException as ve:
                self.update_exception_template(ve)
                return ve

            return None
        return raised_rules_helper

    def should_name_overwritten(self, rule: AbstractRule) -> bool:
        return self._has_name(self) and not self._has_name(rule)

    def _has_name(self, rule) -> bool:
        return rule.get_name() not in [None, '']

    def update_exception_template(self, exception) -> None:
        if self._template is None or exception.has_customer_template():
            return
        exception.update_template(self._template)

        if isinstance(exception, NestedValidationException):
            return

        for ex in exception.get_cheildren():
            self.update_exception_template(ex)
