import re

from respect_validation.Rules.AbstractFilterRule import AbstractFilterRule


class Consonant(AbstractFilterRule):

    def validate_filtered_input(self, input_val) -> bool:
        return bool(re.match(r'^(\s|[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z])*$', input_val))
