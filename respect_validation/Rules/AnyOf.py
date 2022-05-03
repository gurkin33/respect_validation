from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.AbstractComposite import AbstractComposite


class AnyOf(AbstractComposite):

    def claim(self, input_val):
        rules = self.get_rules()
        exceptions = self.get_claim_exception(input_val)
        num_rules = len(rules)
        num_exceptions = len(exceptions)
        if num_exceptions == num_rules:
            any_of_exception = self.report_error(input_val)
            any_of_exception.add_children(exceptions)

            raise any_of_exception

    def validate(self, input_val):
        for rule in self.get_rules():
            if rule.validate(input_val):
                return True

        return False

    def check(self, input_val):
        exceptions = []
        for rule in self.get_rules():
            try:
                rule.check(input_val)
                return
            except ValidationException as e:
                exceptions.append(e)

        raise self.report_error(input_val)
