from typing import Any

from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Helpers.CanCompareValues import CanCompareValues


class AbstractComparison(AbstractRule):

    def __init__(self, max_value: Any):
        super().__init__()
        self.set_param('_compare_to', max_value)

    def compare(self, left: Any, right: Any) -> bool:
        return False

    def validate(self, input_val) -> bool:
        left = CanCompareValues.to_comparable(input_val)
        right = CanCompareValues.to_comparable(self.get_param('_compare_to'))

        if not CanCompareValues.is_able_to_compare(left, right):
            return False

        return self.compare(left, right)
