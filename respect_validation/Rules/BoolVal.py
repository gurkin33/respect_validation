from respect_validation.Rules.AbstractRule import AbstractRule


class BoolVal(AbstractRule):

    def validate(self, input_val) -> bool:
        if isinstance(input_val, str):
            return input_val.lower().strip() in ['0', '1', 'yes', 'no', 'on', 'off', 'true', 'false']
        return input_val in [True, False, 0, 1]
