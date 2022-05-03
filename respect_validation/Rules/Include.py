from typing import Union, List, Any, Tuple

from respect_validation.Rules.AbstractRule import AbstractRule


class Include(AbstractRule):

    _haystack = None
    _identical = None

    def __init__(self, haystack: Union[str, List[Any], Tuple[Any]], identical: bool = True):
        super().__init__()
        self._haystack = haystack
        self._identical = identical

        self.set_param('haystack', haystack)

    def validate(self, input_val):
        if isinstance(self._haystack, list) or isinstance(self._haystack, tuple):
            if self._identical:
                return input_val in self._haystack
            else:
                return any(input_val.lower() in s for s in [x.lower() for x in self._haystack])

        if not isinstance(self._haystack, str) or not isinstance(input_val, str):
            return False

        return self._validate_string(self._haystack, input_val)

    def _validate_string(self, haystack: str, needle: str):

        if needle == '' and haystack == '':
            return True

        if needle == '':
            return False

        if self._identical:
            return needle in haystack

        else:
            return needle.lower() in haystack.lower()
