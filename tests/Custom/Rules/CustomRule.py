from respect_validation.Rules.AbstractRule import AbstractRule


class CustomRule(AbstractRule):

    def validate(self, input_val) -> bool:

        return input_val == 'Hello custom rule!'
