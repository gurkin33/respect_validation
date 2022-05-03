from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Alnum(AbstractFilterRule):

    def validate_filtered_input(self, input_val) -> bool:

        return bool(input_val.isalnum())
