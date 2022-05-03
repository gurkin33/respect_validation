from respect_validation.Rules.AbstractComparison import AbstractComparison


class Max(AbstractComparison):

    @classmethod
    def compare(cls, left: int, right: int) -> bool:
        try:
            return left <= right
        except Exception:
            return False
