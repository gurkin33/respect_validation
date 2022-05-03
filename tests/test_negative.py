import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NegativeException import NegativeException


@pytest.mark.parametrize('value', [
    '-1.44',
    -1e-5,
    -10,
    '-10',
])
def test_success_negative(value):
    assert v.negative().validate(value)
    assert v.negative().check(value) is None
    assert v.negative().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    [],
    object(),
    0,
    -0,
    None,
    'a',
    ' ',
    'Foo',
    16,
    '165',
    123456,
    1e10,
])
def test_fail_negative(value):
    assert v.negative().validate(value) is False

    with pytest.raises(NegativeException, match=r' must be negative'):
        assert v.negative().check(value)
        assert v.negative().claim(value)
