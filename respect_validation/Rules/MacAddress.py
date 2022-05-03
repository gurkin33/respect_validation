import re

from respect_validation.Rules.AbstractRule import AbstractRule


class MacAddress(AbstractRule):

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        return bool(re.match(r'^(([0-9a-fA-F]{2}-){5}|([0-9a-fA-F]{2}:){5})[0-9a-fA-F]{2}$', input_val))
