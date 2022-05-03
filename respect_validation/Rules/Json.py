import json

from respect_validation.Rules.AbstractRule import AbstractRule


class Json(AbstractRule):

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, str) or input_val == '':
            return False

        try:
            json.loads(input_val)
        except Exception:
            return False

        return True
