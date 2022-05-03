from respect_validation.Exceptions import ValidationException
from respect_validation.Rules.AbstractRule import AbstractRule


class Each(AbstractRule):

    _rule: AbstractRule

    def __init__(self, rule: AbstractRule):
        super().__init__()
        self._rule = rule

    def claim(self, input_val):
        if not hasattr(input_val, '__iter__'):
            raise self.report_error(input_val)

        exceptions = []

        for val in input_val:
            try:
                self._rule.claim(val)
            except ValidationException as ve:
                exceptions.append(ve)

        if len(exceptions):
            each_exception = self.report_error(input_val)
            each_exception.add_children(exceptions)  # type: ignore

            raise each_exception

    def validate(self, input_val):

        try:
            self.check(input_val)
        except ValidationException:
            return False

        return True

    def check(self, input_val):

        if not hasattr(input_val, '__iter__'):
            raise self.report_error(input_val)

        for val in input_val:
            self._rule.check(val)
