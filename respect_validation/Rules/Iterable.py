from respect_validation.Rules.AbstractRule import AbstractRule


class Iterable(AbstractRule):

    def validate(self, input_val) -> bool:
        return hasattr(input_val, '__iter__')
