from typing import Union, Set, Any, List, Tuple

from respect_validation.Rules.AbstractRule import AbstractRule


class Subset(AbstractRule):

    _superset: Set[Any]

    def __init__(self, superset: Union[List[Any], Tuple[Any], Set[Any], range]):
        super().__init__()
        self._superset = set(superset)
        self.set_param('superset', superset)

    def validate(self, input_val) -> bool:

        if not isinstance(input_val, list) and not isinstance(input_val, tuple) \
                and not isinstance(input_val, set) and not isinstance(input_val, range):
            return False

        return set(input_val) <= self._superset
