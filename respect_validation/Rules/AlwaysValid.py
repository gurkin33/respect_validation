from respect_validation.Rules.AbstractRule import AbstractRule


class AlwaysValid(AbstractRule):

    def validate(self, input_val):
        return True
