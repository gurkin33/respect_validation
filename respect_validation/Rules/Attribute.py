from typing import Optional

from respect_validation.Rules.AbstractRelated import AbstractRelated
from respect_validation.Rules.AbstractRule import AbstractRule


class Attribute(AbstractRelated):

    def __init__(self, reference: str, rule: Optional[AbstractRule] = None, mandatory: bool = True):
        super().__init__(reference, rule, mandatory)

    def get_reference_value(self, input_val):
        if input_val is None:
            return None
        return getattr(input_val, str(self.get_reference()), None)

    def has_reference(self, input_val):
        return input_val is not None and hasattr(input_val, str(self.get_reference()))
