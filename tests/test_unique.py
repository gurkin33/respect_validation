import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.UniqueException import UniqueException


@pytest.mark.parametrize('value', [
    [1, 2, 3],
    [True, False],
    ['alpha', 'beta', 'gamma', 'delta'],
    [0, 2.71, 3.14],
    [[], ['str'], [1]],
])
def test_success_unique(value):
    assert v.unique().validate(value)
    assert v.unique().check(value) is None
    assert v.unique().claim(value) is None


@pytest.mark.parametrize('value', [
    'test',
    [1, 2, 2, 3],
    [1, 2, 3, 1],
    [True, False, False],
    ['alpha', 'beta', 'gamma', 'delta', 'beta'],
    [0, 3.14, 2.71, 3.14],
    [[], [1], [1]],
])
def test_fail_unique(value):
    assert v.unique().validate(value) is False

    with pytest.raises(UniqueException, match=r' must not contain duplicates'):
        assert v.unique().check(value)
        assert v.unique().claim(value)
