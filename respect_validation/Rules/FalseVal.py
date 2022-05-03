from respect_validation.Rules.AbstractRule import AbstractRule


class FalseVal(AbstractRule):

    def validate(self, input_val):
        if isinstance(input_val, str):
            return input_val.lower() in ['0', 'no', 'off', 'false']
        if isinstance(input_val, int):
            return input_val == 0

        return input_val is False
