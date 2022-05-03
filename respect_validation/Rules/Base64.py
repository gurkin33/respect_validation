import re
from respect_validation.Rules.AbstractRule import AbstractRule


class Base64(AbstractRule):

    def validate(self, input_val):
        if not isinstance(input_val, str):
            return False
        if not bool(re.search(r'^[A-Za-z0-9+/\n\r]+={0,2}$', input_val)):
            return False
        return len(input_val) % 4 == 0
