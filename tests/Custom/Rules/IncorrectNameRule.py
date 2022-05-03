from respect_validation.Rules.AbstractRule import AbstractRule


class CorrectNameRule(AbstractRule):

    def validate(self, input_val) -> bool:

        return input_val == 'I have different names of file and class!'
