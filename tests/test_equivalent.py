import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.EquivalentException import EquivalentException

some_obj = object()


@pytest.mark.parametrize('left,value', [
    [1, True],
    ['Something', 'something'],
    [[1, 2, 3], [1, 2, 3]],
    [some_obj, some_obj],
    [10, 10.0],
])
def test_success_equivalent(left, value):
    assert v.equivalent(left).validate(value)
    assert v.equivalent(left).check(value) is None
    assert v.equivalent(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    ['foo', ''],
    ['foo', 'foo bar'],
    [[1, 2, 3], [1, 2, 3, 4]],
    [10, '10'],
    [1, False],
])
def test_fail_equivalent(left, value):
    assert v.equivalent(left).validate(value) is False

    with pytest.raises(EquivalentException, match=" must be equivalent to "):
        assert v.equivalent(left).check(value)
        assert v.equivalent(left).claim(value)
