from typing import List, Any

from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.AbstractComposite import AbstractComposite


class OneOf(AbstractComposite):

    def claim(self, input_val) -> None:
        rules = self.get_rules()
        exceptions: List[Any] = []
        for r in rules:
            exceptions = exceptions + r.get_claim_exception(input_val)
        num_rules = len(rules)
        num_exceptions = len(exceptions)
        if num_exceptions != (num_rules - 1):
            one_of_exception = self.report_error(input_val)
            one_of_exception.add_children(exceptions)

            raise one_of_exception

    def validate(self, input_val) -> bool:
        rules_passed_count = 0
        for rule in self.get_rules():
            if rule.validate(input_val):
                rules_passed_count += 1

        return rules_passed_count == 1

    def check(self, input_val) -> None:
        exceptions = []
        rules_passed_count = 0
        for rule in self.get_rules():
            try:
                rule.check(input_val)
                rules_passed_count += 1
            except ValidationException as e:
                exceptions.append(e)

        if rules_passed_count == 1:
            return

        raise exceptions[0] if len(exceptions) else self.report_error(input_val)
