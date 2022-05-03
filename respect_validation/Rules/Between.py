from typing import Any

from respect_validation.Exceptions.ComponentException import ComponentException
from respect_validation.Helpers.CanCompareValues import CanCompareValues
from respect_validation.Rules.AbstractEnvelope import AbstractEnvelope
from respect_validation.Rules.AllOf import AllOf
from respect_validation.Rules.Max import Max
from respect_validation.Rules.Min import Min


class Between(AbstractEnvelope):

    def __init__(self, min_val: Any, max_val: Any):
        if CanCompareValues.to_comparable(min_val) >= CanCompareValues.to_comparable(max_val):
            raise ComponentException("Minimum value cannot be more than or equals to maximum") from None

        super().__init__(AllOf(
            Min(min_val),
            Max(max_val)
        ), {
            "min_value": min_val,
            "max_value": max_val
        })
