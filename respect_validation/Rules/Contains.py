from respect_validation.Rules.AbstractRule import AbstractRule


class Contains(AbstractRule):

    _contains_value = None
    _identical = None

    def __init__(self, contains_value, identical: bool = True):
        super().__init__()
        self._contains_value = contains_value
        self._identical = identical
        self.set_param('contains_value', contains_value)

    def validate(self, input_val) -> bool:

        if hasattr(input_val, '__iter__') and not isinstance(input_val, str):
            return self._contains_value in input_val

        if not isinstance(input_val, str) or not isinstance(self._contains_value, str):
            return False

        if self._identical and self._contains_value != '':
            return self._contains_value in input_val

        return self._validate_string(input_val, self._contains_value)

    def _validate_string(self, haystack: str, needle: str) -> bool:

        if needle == '':
            return False

        if self._identical:
            return needle in haystack

        else:
            return needle.lower() in haystack.lower()
