from respect_validation.Rules.AbstractRule import AbstractRule


class BytearrayType(AbstractRule):

    def validate(self, input_val) -> bool:

        return isinstance(input_val, bytearray)
