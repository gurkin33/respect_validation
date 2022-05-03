from respect_validation.Rules.AbstractRule import AbstractRule


class TrueVal(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, str):
            return input_val.lower() in ['1', 'yes', 'on', 'true']
        if isinstance(input_val, int):
            return input_val == 1

        return input_val is True
