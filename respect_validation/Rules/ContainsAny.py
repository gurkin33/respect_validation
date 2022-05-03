from typing import List, Any

from respect_validation.Rules.AbstractEnvelope import AbstractEnvelope
from respect_validation.Rules.AbstractRule import AbstractRule
from respect_validation.Rules.AnyOf import AnyOf
from respect_validation.Rules.Contains import Contains


class ContainsAny(AbstractEnvelope):

    def __init__(self, needles: List[Any], identical: bool = True):
        super().__init__(
            AnyOf(*self._get_rules(needles, identical)), {'needles': needles}
        )

    def _get_rules(self, needles, identical) -> List[AbstractRule]:
        if hasattr(needles, '__iter__') and not isinstance(needles, str):
            return [Contains(n, identical) for n in needles]
        return [Contains(needles, identical)]
