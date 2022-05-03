from respect_validation.Rules.AbstractRule import AbstractRule


class ListType(AbstractRule):

    def validate(self, input_val):
        return isinstance(input_val, list)
