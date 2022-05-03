import random

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FalseValException import FalseValException


@pytest.mark.parametrize('value', [
    False,
    0,
    '0',
    'false',
    'False',
    'FALSE',
    'no',
    'NO',
    'No',
    'off',
    'ofF',
    'OFF',
])
def test_success_falseVal(value):
    assert v.falseVal().validate(value)
    assert v.falseVal().check(value) is None
    assert v.falseVal().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    True,
    random.randint(1, 10000000000),
    str(random.randint(1, 10000000000)),
    0.5,
    'true',
    'on',
    'yes',
    'anything',
    [],
    object()
])
def test_fail_falseVal(value):
    assert v.falseVal().validate(value) is False

    with pytest.raises(FalseValException, match=r' is not considered as "False"'):
        assert v.falseVal().check(value)
        assert v.falseVal().claim(value)
