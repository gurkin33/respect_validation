import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Slug(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str) or '--' in input_val:
            return False

        if not re.match(r'^[0-9a-z\-]+$', input_val):
            return False

        return not bool(re.search('^-|-$', input_val))
