import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Nip(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, int):
            input_val = str(input_val)

        if not isinstance(input_val, str):
            return False

        if not bool(re.match(r'^\d{10}$', input_val)):
            return False

        weights = [6, 5, 7, 2, 3, 4, 5, 6, 7]
        digits = [int(d) for d in input_val]

        target_control_number = digits[9]
        calculate_control_number = 0

        for i in range(9):
            calculate_control_number += digits[i] * weights[i]

        calculate_control_number = calculate_control_number % 11

        return target_control_number == calculate_control_number
