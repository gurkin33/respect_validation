import math

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.InfiniteException import InfiniteException


@pytest.mark.parametrize('value', [
    math.inf,
    math.inf * -1,
])
def test_success_infinite(value):
    assert v.infinite().validate(value)
    assert v.infinite().check(value) is None
    assert v.infinite().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    123456789,
    True,
    None,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
])
def test_fail_infinite(value):
    assert v.infinite().validate(value) is False

    with pytest.raises(InfiniteException, match=r' must be an infinite number'):
        assert v.infinite().check(value)
        assert v.infinite().claim(value)
