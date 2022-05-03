from string import punctuation

from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Punct(AbstractFilterRule):

    def validate_filtered_input(self, input_val) -> bool:

        if not isinstance(input_val, str):
            return False

        for c in input_val:
            if c not in punctuation:
                return False

        return True
