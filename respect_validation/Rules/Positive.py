from respect_validation.Rules.AbstractRule import AbstractRule


class Positive(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, int) or isinstance(input_val, float) or\
                isinstance(input_val, str) and input_val.isdigit():

            return int(input_val) > 0

        return False
