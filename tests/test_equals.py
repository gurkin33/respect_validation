import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.EqualsException import EqualsException

some_obj = object()


@pytest.mark.parametrize('left,value', [
    ['foo', 'foo'],
    [[], []],
    [some_obj, some_obj],
    [10, 10.0],
])
def test_success_equals(left, value):
    assert v.equals(left).validate(value)
    assert v.equals(left).check(value) is None
    assert v.equals(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    ['foo', ''],
    ['foo', 'bar'],
    [10, '10'],
    [10, []],
    [object(), []],
])
def test_fail_equals(left, value):
    assert v.equals(left).validate(value) is False

    with pytest.raises(EqualsException, match=" must be equal to "):
        assert v.equals(left).check(value)
        assert v.equals(left).claim(value)
