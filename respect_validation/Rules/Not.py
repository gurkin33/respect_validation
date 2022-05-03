from respect_validation.Exceptions.ValidationException import ValidationException
from respect_validation.Rules.AbstractComposite import AbstractComposite
from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.AllOf import AllOf


class Not(AbstractRule):

    def __init__(self, rule: AbstractRule):
        super().__init__()
        self.rule = self._extract_negated_rule(rule)

    def get_negative_rule(self):
        return self.rule

    def set_name(self, name):
        self.rule.set_name(name)

        return super().set_name(name)

    def validate(self, input_val):

        return self.rule.validate(input_val) is False

    def claim(self, input_val):
        if self.validate(input_val):
            return
        rule = self.rule
        if isinstance(rule, AllOf):
            rule = self._absorb_all_of(rule, input_val)

        exception = rule.report_error(input_val)
        exception.update_mode(ValidationException.MODE_NEGATIVE)

        raise exception

    def _absorb_all_of(self, rule, input_val):
        rules = rule.get_rules()
        while rules:
            rule = rules.pop(0)
            if not isinstance(rule, AllOf):
                continue

            if not rule.validate(input_val):
                continue

            rules = rule.get_rules()

        return rule

    def _extract_negated_rule(self, rule: AbstractRule):

        if isinstance(rule, Not) and isinstance(rule.get_negative_rule(), Not):
            return self._extract_negated_rule(rule.get_negative_rule().get_negative_rule())

        if not isinstance(rule, AbstractComposite):
            return rule

        rules = rule.get_rules()

        if len(rules) == 1:
            return self._extract_negated_rule(rules[0])

        return rule
