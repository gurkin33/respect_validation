from respect_validation.Rules.AbstractRule import AbstractRule


class Fibonacci(AbstractRule):

    def validate(self, input_val):

        if isinstance(input_val, str) and input_val.isdigit():
            input_val = int(input_val)

        if not isinstance(input_val, int) and not isinstance(input_val, float):
            return False

        sequence = [0, 1]
        position = 1

        while input_val > sequence[position]:
            position += 1
            sequence.append(sequence[position - 1] + sequence[position - 2])

        return sequence[position] == input_val
