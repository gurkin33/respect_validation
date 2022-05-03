import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LengthException import LengthException


@pytest.mark.parametrize('params, value', [
    [(1, 15), 'alganet'],
    [(4, 6), 'ççççç'],
    [(1, 30), range(1, 20)],
    [(0, 2), {'foo': 'bar', 'bar': 'baz'}],
    [(1, None), 'alganet'],  # None is a valid max length, means "no maximum",
    [(None, 15), 'alganet'],  # None is a valid min length, means "no minimum"
    [(1, 15, False), 'alganet'],
    [(4, 6, False), 'ççççç'],
    [(1, 30, False), range(1, 20)],
    [(1, 3, False), {'foo': 'bar', 'bar': 'baz'}],
    [(1, None, False), 'alganet'],  # None is a valid max length, means "no maximum",
    [(None, 15, False), 'alganet'],  # None is a valid min length, means "no minimum"
    [(1, 15), range(5)],
    [(1, 15), 12345],
])
def test_success_length(params, value):
    assert v.length(*params).validate(value)
    assert v.length(*params).check(value) is None
    assert v.length(*params).claim(value) is None


@pytest.mark.parametrize('params, value', [
    [(1, 15), ''],
    [(1, 6), 'alganet'],
    [(1, 19, False), range(1, 20)],
    [(8, None), 'alganet'],  # None is a valid max length, means "no maximum",
    [(None, 6), 'alganet'],  # None is a valid min length, means "no minimum"
    [(1, 7, False), 'alganet'],
    [(3, 5, False), {'foo': 'bar', 'bar': 'baz'}],
    [(1, 30, False), range(1, 50)],
    [(1, 4), range(5)],
    [(1, 4), 12345],
])
def test_fail_length(params, value):
    assert v.length(*params).validate(value) is False

    with pytest.raises(LengthException, match=r' must have a length '):
        assert v.length(*params).check(value)
        assert v.length(*params).claim(value)
