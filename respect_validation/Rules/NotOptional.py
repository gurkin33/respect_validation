from respect_validation.Rules.AbstractRule import AbstractRule


class NotOptional(AbstractRule):
    def validate(self, input_val) -> bool:

        return input_val not in ['', None]
