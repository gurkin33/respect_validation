import re

from respect_validation.Rules.AbstractRule import AbstractRule


class NoWhitespace(AbstractRule):

    def validate(self, input_val) -> bool:
        if input_val is None:
            return True

        if not isinstance(input_val, str) and not hasattr(input_val, '__str__'):
            return False

        return not bool(re.search(r"\s", str(input_val)))
