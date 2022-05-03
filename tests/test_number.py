import math

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NumberException import NumberException


@pytest.mark.parametrize('value', [
    '42',
    123456,
    0.00000000001,
    '0.5',
    math.inf,
    -math.inf,
    True,
    False,
])
def test_success_number(value):
    assert v.number().validate(value)
    assert v.number().check(value) is None
    assert v.number().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    object(),
    math.nan,
    -math.nan,
    'nan'
])
def test_fail_number(value):
    assert v.number().validate(value) is False

    with pytest.raises(NumberException, match=r' must be number'):
        assert v.number().check(value)
        assert v.number().claim(value)
