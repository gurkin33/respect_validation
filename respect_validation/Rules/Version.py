import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Version(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str):
            return False

        return bool(re.search(r'^[0-9]+\.[0-9]+\.[0-9]+([+-][^+-][0-9A-Za-z-.]*)?$', input_val))
