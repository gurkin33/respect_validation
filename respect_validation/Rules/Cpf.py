import re

from respect_validation.Rules.AbstractRule import AbstractRule


class Cpf(AbstractRule):

    def validate(self, input_val):
        c = str(re.sub(r'[^0-9]', "", input_val))

        if len(c) != 11 or re.findall(r'^'+c[0]+'{11}$', c) or c == '01234567890':
            return False

        n = 0
        i = 0
        for s in reversed(range(2, 11)):
            n += int(c[i]) * s
            i += 1
        n = n % 11

        if int(c[9]) != (0 if n < 2 else (11 - n)):
            return False

        n = 0
        i = 0
        for s in reversed(range(2, 12)):
            n += int(c[i]) * s
            i += 1
        n = n % 11

        check = 0 if n < 2 else (11 - n)

        return int(c[10]) == check
