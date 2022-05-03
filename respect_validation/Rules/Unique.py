from respect_validation.Rules.AbstractRule import AbstractRule


class Unique(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, list) and not isinstance(input_val, tuple):
            return False

        return len(set(map(str, input_val))) == len(input_val)
