from respect_validation.Rules.AbstractComposite import AbstractComposite


class NoneOf(AbstractComposite):

    def claim(self, input_val) -> None:
        exceptions = self.get_claim_exception(input_val)
        num_rules = len(self.get_rules())
        num_exceptions = len(exceptions)
        if num_rules != num_exceptions:
            none_of_exception = self.report_error(input_val)
            none_of_exception.add_children(exceptions)

            raise none_of_exception

    def validate(self, input_val) -> bool:

        for rule in self.get_rules():
            if rule.validate(input_val):
                return False

        return True
