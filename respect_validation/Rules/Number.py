import math
from typing import Union

from respect_validation.Rules.AbstractRule import AbstractRule


class Number(AbstractRule):

    def validate(self, input_val: Union[str, int, float]) -> bool:

        if isinstance(input_val, float) and math.isnan(input_val):
            return False

        if isinstance(input_val, int) or isinstance(input_val, float) or \
                (isinstance(input_val, str) and input_val.isdigit()):
            return True

        if isinstance(input_val, str) and input_val != 'nan':
            try:
                float(input_val)
                return True
            except Exception:
                return False
        return False
