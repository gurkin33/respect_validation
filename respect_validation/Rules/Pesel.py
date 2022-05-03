import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Pesel(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, int):
            input_val = str(input_val)

        if not isinstance(input_val, str):
            return False

        if not re.match(r'^\d{11}$', input_val):
            return False

        weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        target_control_number = input_val[10]
        calculated_control_number = 0

        for i in range(10):
            calculated_control_number += int(input_val[i]) * weights[i]

        calculated_control_number = (10 - calculated_control_number % 10) % 10

        return int(calculated_control_number) == int(target_control_number)
