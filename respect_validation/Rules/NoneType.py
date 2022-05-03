from respect_validation.Rules.AbstractRule import AbstractRule


class NoneType(AbstractRule):

    def validate(self, input_val) -> bool:

        return input_val is None
