import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Yes(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str):
            return False

        return bool(re.match(r'^y(eah?|ep|es)?$', input_val.lower()))
