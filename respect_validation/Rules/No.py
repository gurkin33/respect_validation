import re

from respect_validation.Rules.AbstractRule import AbstractRule


class No(AbstractRule):

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        return bool(re.match(r'^n(o(t|pe)?|ix|ay)?$', input_val.lower()))
