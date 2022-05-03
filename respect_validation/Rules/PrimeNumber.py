from respect_validation.Rules.AbstractRule import AbstractRule


class PrimeNumber(AbstractRule):

    def validate(self, input_val) -> bool:

        if isinstance(input_val, int) or isinstance(input_val, str) and input_val.isdigit():
            return self._is_prime(int(input_val))

        return False

    def _is_prime(self, input_val: int) -> bool:

        if input_val == 2 or input_val == 3:
            return True
        if input_val % 2 == 0 or input_val < 2:
            return False

        for n in range(3, int(input_val ** 0.5) + 1, 2):
            if input_val % n == 0:
                return False
        return True
