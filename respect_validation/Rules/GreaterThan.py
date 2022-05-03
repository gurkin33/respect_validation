from respect_validation.Rules.AbstractComparison import AbstractComparison


class GreaterThan(AbstractComparison):

    def compare(self, left, right) -> bool:
        try:
            return bool(left > right)
        except Exception:
            return False
