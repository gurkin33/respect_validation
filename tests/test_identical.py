import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IdenticalException import IdenticalException


@pytest.mark.parametrize('left,value', [
    ['foo', 'foo'],
    [[], []],
    [10, 10],
    [10.0, 10.0],
    [True, True],
    [dict(), dict()]
])
def test_success_identical(left, value):
    assert v.identical(left).validate(value)
    assert v.identical(left).check(value) is None
    assert v.identical(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    [42, '42'],
    ['foo', 'bar'],
    [1, True],
    [0, False],
    [[1], []],
    [object(), object()],
    [10, 10.0],
])
def test_fail_identical(left, value):
    assert v.identical(left).validate(value) is False

    with pytest.raises(IdenticalException, match=r' must be identical as '):
        assert v.identical(left).check(value)
        assert v.identical(left).claim(value)
