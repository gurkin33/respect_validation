from respect_validation.Rules.AbstractRule import AbstractRule


class StringVal(AbstractRule):

    def validate(self, input_val) -> bool:

        return isinstance(input_val, str) or hasattr(input_val, '__str__')
