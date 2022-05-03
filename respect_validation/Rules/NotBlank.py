from respect_validation.Rules.AbstractRule import AbstractRule


class NotBlank(AbstractRule):

    def validate(self, input_val) -> bool:

        if input_val is None:
            return False

        if isinstance(input_val, bool):
            return input_val

        if isinstance(input_val, int) or isinstance(input_val, str) and input_val.isdigit():
            return int(input_val) != 0

        if isinstance(input_val, str):
            return bool(input_val.strip())

        if isinstance(input_val, dict):
            return bool(len(input_val.keys()))

        if isinstance(input_val, list):
            return bool(len(list(filter(lambda el: el not in ['', 0, '0', None, False], input_val))))

        return False
