from respect_validation.Rules.AbstractRule import AbstractRule


class BytesType(AbstractRule):

    def validate(self, input_val) -> bool:

        return isinstance(input_val, bytes)
