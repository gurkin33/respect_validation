from respect_validation.Rules.AbstractRule import AbstractRule


class NoExceptionRule(AbstractRule):

    def validate(self, input_val) -> bool:

        return input_val == 'I do not have exception!'
