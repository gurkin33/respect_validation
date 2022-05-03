from respect_validation.Rules.AbstractRule import AbstractRule


class NotEmpty(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, str):
            return bool(input_val.strip())

        try:
            return bool(input_val)
        except Exception:
            return True
