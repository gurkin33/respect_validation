import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.EndsWithException import EndsWithException


@pytest.mark.parametrize('params,value', [
    [('foo',), ['bar', 'foo']],
    [('foo',), 'barbazfoo'],
    [('foo',), 'foobazfoo'],
    [(1,), [2, 3, 1]],
    [('1', ), [2, 3, '1']],
])
def test_success_endsWith(params, value):
    assert v.endsWith(*params).validate(value)
    assert v.endsWith(*params).check(value) is None
    assert v.endsWith(*params).claim(value) is None


@pytest.mark.parametrize('params,value', [
    [('foo',), ''],
    [('foo',), 'barbazFOO'],
    [('bat',), ['bar', 'foo']],
    [('foo',), 'barfaabaz'],
    [('foo',), 'barbazFOO'],
    [('foo',), 'faabarbaz'],
    [('foo',), 'baabazfaa'],
    [('foo',), 'baafoofaa'],
    [('1',), [2, 3, 1]],
    [('1',), [1, '1', 3]],
])
def test_fail_endsWith(params, value):
    assert v.endsWith(*params).validate(value) is False

    with pytest.raises(EndsWithException, match="must end with "):
        assert v.endsWith(*params).check(value)
        assert v.endsWith(*params).claim(value)
