from respect_validation.Rules.AbstractRule import AbstractRule


class AbstractWrapper(AbstractRule):

    _rule: AbstractRule

    def __init__(self, rule: AbstractRule):
        super().__init__()
        self._rule = rule

    def claim(self, input_val) -> None:
        self._rule.claim(input_val)

    def check(self, input_val) -> None:
        self._rule.check(input_val)

    def validate(self, input_val) -> bool:
        return self._rule.validate(input_val)

    def set_name(self, name: str):
        self._rule.set_name(name)
        return super().set_name(name)
