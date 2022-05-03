import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PrimeNumberException import PrimeNumberException


@pytest.mark.parametrize('value', [
    3,
    5,
    7,
    '3',
    '5',
])
def test_success_primeNumber(value):
    assert v.primeNumber().validate(value)
    assert v.primeNumber().check(value) is None
    assert v.primeNumber().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    None,
    0,
    10,
    25,
    36,
    -1,
    '+7',
    '-1',
    '25',
    '0',
    'a',
    ' ',
    'Foo',
])
def test_fail_primeNumber(value):
    assert v.primeNumber().validate(value) is False

    with pytest.raises(PrimeNumberException, match=r' must be a valid prime number'):
        assert v.primeNumber().check(value)
        assert v.primeNumber().claim(value)
