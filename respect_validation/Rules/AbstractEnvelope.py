from typing import Dict, Any

from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractEnvelope(AbstractRule):

    def __init__(self, rule, params: Dict[str, Any] = {}):
        super().__init__()
        self.envelop_rule = rule
        self.envelop_params = params

    def validate(self, input_val):
        return self.envelop_rule.validate(input_val)

    def report_error(self, input_val, extra_params: Dict[str, Any] = {}):
        return super().report_error(input_val, {**extra_params, **self.envelop_params})
