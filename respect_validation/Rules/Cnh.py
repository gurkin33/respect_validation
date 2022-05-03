import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Cnh(AbstractRule):

    def validate(self, input_val):

        if not isinstance(input_val, str):
            return False

        input_val = re.sub("[^0-9]", "", input_val)

        if len(input_val) != 11 or int(input_val) == 0:
            return False

        s1 = 0
        s2 = 0
        p = 9

        for c in range(9):
            s1 += int(input_val[c]) * p
            s2 += int(input_val[c]) * (10 - p)
            p -= 1

        dv1 = s1 % 11
        dv1_tmp = 0 if dv1 > 9 else dv1
        if int(input_val[9]) != dv1_tmp:
            return False

        dv1_tmp = 2 if dv1 > 9 else 0
        dv2 = s2 % 11 - dv1_tmp
        check = (dv2 + 11) if dv2 < 0 else 0 if dv2 > 9 else dv2
        return int(input_val[10]) == check
