import unicodedata

from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Control(AbstractFilterRule):

    def validate_filtered_input(self, input_val: str) -> bool:
        for ch in input_val:
            if unicodedata.category(ch)[0] != "C":
                return False
        return True
