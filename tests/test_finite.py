import math

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FiniteException import FiniteException


@pytest.mark.parametrize('value', [
    '123456',
    '123.456',
    0,
    -1,
    1.3e100,
    1.3e100 * -1,
    True,
    False
])
def test_success_finite(value):
    assert v.finite().validate(value)
    assert v.finite().check(value) is None
    assert v.finite().claim(value) is None


@pytest.mark.parametrize('value', [
    'anything',
    [],
    object(),
    math.inf,
    None
])
def test_fail_finite(value):
    assert v.finite().validate(value) is False

    with pytest.raises(FiniteException, match=r'must be a finite'):
        assert v.finite().check(value)
        assert v.finite().claim(value)
