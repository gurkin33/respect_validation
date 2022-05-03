import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.StartsWithException import StartsWithException


@pytest.mark.parametrize('starts,value', [
    ['foo', ['foo', 'bar']],
    ['foo', 'foobarbaz'],
    ['foo', 'foobazfoo'],
    ['1', ['1', 2, 3]],
])
def test_success_startsWith(starts, value):
    assert v.startsWith(starts).validate(value)
    assert v.startsWith(starts).check(value) is None
    assert v.startsWith(starts).claim(value) is None


@pytest.mark.parametrize('starts,value', [
    ['foo', ''],
    ['bat', ['foo', 'bar']],
    ['foo', 'barfaabaz'],
    ['foo', 'FOObarbaz'],
    ['foo', 'faabarbaz'],
    ['foo', 'baabazfaa'],
    ['foo', 'baafoofaa'],
    ['1', [1, '1', 3]],
])
def test_fail_startsWith(starts, value):
    assert v.startsWith(starts).validate(value) is False

    with pytest.raises(StartsWithException, match=r' must start with'):
        assert v.startsWith(starts).check(value)
        assert v.startsWith(starts).claim(value)
