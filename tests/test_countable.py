import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.CountableException import CountableException


@pytest.mark.parametrize('value', [
    '',
    'abcd',
    [],
    [1, 2, 3, 4],
    {1, 2, 3},
    ('a', 'b', 'c'),
    {"hello": "world"},
    range(10)
])
def test_success_countable(value):
    assert v.countable().validate(value)
    assert v.countable().check(value) is None
    assert v.countable().claim(value) is None


@pytest.mark.parametrize('value', [
    1.1,
    -12,
    None,
    True,
    object()
])
def test_fail_countable(value):
    assert v.countable().validate(value) is False

    with pytest.raises(CountableException, match="must be countable"):
        assert v.countable().check(value)
        assert v.countable().claim(value)
