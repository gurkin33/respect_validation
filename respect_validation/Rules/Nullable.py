from respect_validation.Rules.AbstractWrapper import AbstractWrapper


class Nullable(AbstractWrapper):

    def claim(self, input_val) -> None:
        if input_val is None:
            return
        super().claim(input_val)

    def check(self, input_val) -> None:
        if input_val is None:
            return
        super().check(input_val)

    def validate(self, input_val) -> bool:
        if input_val is None:
            return True
        return super().validate(input_val)
