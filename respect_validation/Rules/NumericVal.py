from respect_validation.Rules.AbstractRule import AbstractRule


class NumericVal(AbstractRule):

    def validate(self, input_val) -> bool:

        # if it is int or float or str which can be treated as int, then True
        if isinstance(input_val, int) or isinstance(input_val, float) or \
                isinstance(input_val, str) and input_val.isdigit():
            return True
        # if we still have str we will try to convert it to float
        if isinstance(input_val, str):
            try:
                float(input_val)
                return True
            except Exception:
                return False
        return False
