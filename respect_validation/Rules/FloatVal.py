from respect_validation.Rules.AbstractRule import AbstractRule


class FloatVal(AbstractRule):

    def validate(self, input_val):
        if isinstance(input_val, str) and not input_val.isdigit():
            try:
                float(input_val)
                return True
            except Exception:
                return False

        return isinstance(input_val, float)
