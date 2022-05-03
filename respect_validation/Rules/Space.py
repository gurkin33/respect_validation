import re

from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Space(AbstractFilterRule):

    def validate_filtered_input(self, input_val):

        if not isinstance(input_val, str):
            return False

        return bool(re.search(r"^[\r\n\s\t]+$", input_val))
