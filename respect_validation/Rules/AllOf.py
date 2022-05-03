from respect_validation.Rules.AbstractComposite import AbstractComposite


class AllOf(AbstractComposite):

    def check(self, input_val):
        for rule in self.get_rules():
            rule.check(input_val)

    def validate(self, input_val) -> bool:
        for rule in self.get_rules():
            if not rule.validate(input_val):
                return False
        return True

    def claim(self, input_val):
        exceptions = self.get_claim_exception(input_val)
        summary = {
            'total': len(self.get_rules()),
            'failed': len(exceptions),
            'passed': len(self.get_rules()) - len(exceptions),
            'rules': self.get_rules()
        }
        if len(exceptions) != 0:
            all_of_exceptions = self.report_error(input_val, summary)
            all_of_exceptions.add_children(exceptions)
            all_of_exceptions.refresh_template()
            raise all_of_exceptions
