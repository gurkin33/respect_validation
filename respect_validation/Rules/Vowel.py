import re

from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Vowel(AbstractFilterRule):

    def validate_filtered_input(self, input_val) -> bool:
        return bool(re.search(r'^[aeiouAEIOU]+$', input_val))
