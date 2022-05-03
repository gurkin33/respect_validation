from typing import Any

from respect_validation.Exceptions import ComponentException, ValidationException
from respect_validation.Factory import Factory
from respect_validation.Rules.AbstractRule import AbstractRule


class KeyValue(AbstractRule):

    _compared_key = None
    _rule_name = None
    _base_key = None

    def __init__(self, compared_key: str, rule_name: str, base_key: str):
        super().__init__()
        self._compared_key = compared_key
        self._rule_name = rule_name
        self._base_key = base_key

        self.set_param('compared_key', compared_key)
        self.set_param('base_key', base_key)

    def claim(self, input_val) -> None:
        rule = self._get_rule(input_val)

        try:
            rule.claim(input_val[self._compared_key])
        except ValidationException as exception:
            raise self._overwrite_exception_params(exception) from None

    def check(self, input_val) -> None:
        rule = self._get_rule(input_val)

        try:
            rule.check(input_val[self._compared_key])
        except ValidationException as exception:
            raise self._overwrite_exception_params(exception) from None

    def validate(self, input_val) -> bool:

        try:
            rule = self._get_rule(input_val)
        except ValidationException:
            return False

        return bool(rule.validate(input_val[self._compared_key]))

    def _get_rule(self, input_value) -> Any:

        if not isinstance(input_value, dict):
            raise ComponentException('KeyValue rule can validate only dict type') from None

        if self._compared_key not in input_value.keys():
            raise super().report_error(self._compared_key)

        if self._base_key not in input_value.keys():
            raise super().report_error(self._base_key)

        try:
            rule = Factory.get_default_instance().rule(self._rule_name, input_value[self._base_key])
            rule.set_name(self._compared_key)
        except Exception:
            raise super().report_error(input_value, {'component': True})

        return rule

    def _overwrite_exception_params(self, exception: ValidationException) -> ValidationException:
        params = {}

        for key in exception.get_params():
            if key in ['template', 'translator']:
                continue
            params[key] = self._base_key
        params['name'] = self._compared_key

        exception.update_params(params)

        return exception
