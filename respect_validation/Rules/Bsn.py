from respect_validation.Rules.AbstractRule import AbstractRule


class Bsn(AbstractRule):

    def validate(self, input_val):
        input_val = str(input_val)
        if not input_val.isdigit():
            return False

        if len(input_val) != 9:
            return False

        bsn_sum = -1 * int(input_val[8])
        for i in reversed(range(2, 10)):
            bsn_sum += i * int(input_val[9-i])
        return bsn_sum != 0 and bsn_sum % 11 == 0
