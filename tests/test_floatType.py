import math

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FloatTypeException import FloatTypeException


@pytest.mark.parametrize('value', [
    165.23,
    7E-10,
    0.0,
    -1.44,
    1.3e100,
    1.3e100 * -1,
    10 / 33.33,
    math.inf,
])
def test_success_floatType(value):
    assert v.floatType().validate(value)
    assert v.floatType().check(value) is None
    assert v.floatType().claim(value) is None


@pytest.mark.parametrize('value', [
    1,
    111111111,
    '1',
    '1.0',
    '7E-10',
    'anything',
    [],
    object(),
    None
])
def test_fail_floatType(value):
    assert v.floatType().validate(value) is False

    with pytest.raises(FloatTypeException, match=r'must be of type float'):
        assert v.floatType().check(value)
        assert v.floatType().claim(value)
