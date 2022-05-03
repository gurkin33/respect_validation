from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Digit(AbstractFilterRule):

    def validate_filtered_input(self, input_val):
        return input_val.isdigit()
