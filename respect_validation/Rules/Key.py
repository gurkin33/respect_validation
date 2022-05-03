from respect_validation.Exceptions import ComponentException
from respect_validation.Rules.AbstractRelated import AbstractRelated


class Key(AbstractRelated):

    def __init__(self, reference: str, rule=None, mandatory: bool = True):

        if not isinstance(reference, str) or reference == '':
            raise ComponentException('Invalid array key name') from None
        super().__init__(reference, rule, mandatory)

    def get_reference_value(self, input_val):
        return input_val.get(self.get_reference(), None)

    def has_reference(self, input_val):
        return isinstance(input_val, dict) and self.get_reference() in input_val.keys()
