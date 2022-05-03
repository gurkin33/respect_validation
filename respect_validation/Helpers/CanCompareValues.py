from datetime import datetime


class CanCompareValues:

    @classmethod
    def to_comparable(cls, value):
        if isinstance(value, int) or isinstance(value, float) or \
                (isinstance(value, str) and len(value) == 1 and not value.isdigit())\
                or isinstance(value, datetime):
            return value

        try:
            return datetime.fromisoformat(value)
        except Exception:
            pass

        if isinstance(value, str) and value.isdigit():
            return int(value)

        if hasattr(value, '__len__'):
            return len(value)

        return value

    @classmethod
    def is_able_to_compare(cls, left, right):
        return type(left) in [int, str, float, bool, list, tuple, set, range, datetime] and \
               type(right) in [int, str, float, bool, list, tuple, set, range, datetime]
