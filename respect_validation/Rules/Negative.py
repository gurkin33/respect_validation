from respect_validation.Rules.AbstractRule import AbstractRule


class Negative(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, int) and not isinstance(input_val, float) and not isinstance(input_val, str):
            return False

        if isinstance(input_val, str):
            if input_val.isdigit():
                input_val = int(input_val)
            else:
                try:
                    input_val = float(input_val)
                except Exception:
                    return False

        return bool(input_val < 0)
