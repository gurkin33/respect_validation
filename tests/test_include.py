import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IncludeException import IncludeException


@pytest.mark.parametrize('left,value', [
    [('', ), ''],
    [([None], ), None],
    [(['0'], ), '0'],
    [([0], ), 0],
    [(['foo', 'bar'], ), 'foo'],
    [('barfoobaz', ), 'foo'],
    [('foobarbaz', ), 'foo'],
    [('barbazfoo', ), 'foo'],
    [(['1', 2, 3], True, ), '1'],
])
def test_success_include(left, value):
    assert v.include(*left).validate(value)
    assert v.include(*left).check(value) is None
    assert v.include(*left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    [('0', ), None],
    [(0, True, ), None],
    [('', True, ), None],
    [([], True, ), None],
    [('barfoobaz', ), ''],
    [('barfoobaz', ), None],
    [('barfoobaz', ), 0],
    [('barfoobaz', ), '0'],
    [(['foo', 'bar'], ), 'bat'],
    [('barfaabaz', ), 'foo'],
    [('faabarbaz', ), 'foo'],
    [('baabazfaa', ), 'foo'],
    [([1, 2, 3],), '1'],
    [([1, 2, 3], True, ), '1'],
])
def test_fail_include(left, value):
    assert v.include(*left).validate(value) is False

    with pytest.raises(IncludeException, match=r' must be in '):
        assert v.include(*left).check(value)
        assert v.include(*left).claim(value)
