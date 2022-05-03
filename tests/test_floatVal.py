import math

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FloatValException import FloatValException


@pytest.mark.parametrize('value', [
    '1.0',
    '7E-10',
    165.23,
    7E-10,
    0.0,
    -1.44,
    1.3e100,
    1.3e100 * -1,
    10 / 33.33,
    math.inf,
])
def test_success_floatVal(value):
    assert v.floatVal().validate(value)
    assert v.floatVal().check(value) is None
    assert v.floatVal().claim(value) is None


@pytest.mark.parametrize('value', [
    1,
    111111111,
    '1',
    '15',
    'anything',
    [],
    object(),
    None
])
def test_fail_floatVal(value):
    assert v.floatVal().validate(value) is False

    with pytest.raises(FloatValException, match=r' must be a float number'):
        assert v.floatVal().check(value)
        assert v.floatVal().claim(value)
