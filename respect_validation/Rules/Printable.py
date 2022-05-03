from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Printable(AbstractFilterRule):

    def validate_filtered_input(self, input_val: str) -> bool:

        return isinstance(input_val, str) and input_val.isprintable()
