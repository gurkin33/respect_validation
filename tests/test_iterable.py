import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IterableException import IterableException


@pytest.mark.parametrize('value', [
    [1, 2, 3],
    (1, 2, 3),
    {"name": "alex"},
    set(),
    list(),
    tuple(),
    'abc',
    str()
])
def test_success_iterable(value):
    assert v.iterable().validate(value)
    assert v.iterable().check(value) is None
    assert v.iterable().claim(value) is None


@pytest.mark.parametrize('value', [
    True,
    1,
    0.1,
    False,
    None,
    object(),
])
def test_fail_iterable(value):
    assert v.iterable().validate(value) is False

    with pytest.raises(IterableException, match=r' must be iterable'):
        assert v.iterable().check(value)
        assert v.iterable().claim(value)
