import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PerfectSquareException import PerfectSquareException


@pytest.mark.parametrize('value', [
    1,
    9,
    25,
    '25',
    400,
    '400',
    '0',
    81,
    0,
    2500,
])
def test_success_perfectSquare(value):
    assert v.perfectSquare().validate(value)
    assert v.perfectSquare().check(value) is None
    assert v.perfectSquare().claim(value) is None


@pytest.mark.parametrize('value', [
    250,
    '',
    None,
    7,
    -1,
    6,
    2,
    '-1',
    'a',
    ' ',
    'Foo',
])
def test_fail_perfectSquare(value):
    assert v.perfectSquare().validate(value) is False

    with pytest.raises(PerfectSquareException, match=r' must be a valid perfect square'):
        assert v.perfectSquare().check(value)
        assert v.perfectSquare().claim(value)
