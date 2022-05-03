import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FibonacciException import FibonacciException


@pytest.mark.parametrize('value', [
    1,
    2,
    3,
    5,
    8.0,
    '3',
    21,
    21.0,
    34,
    '34',
    1346269,
    10610209857723,
    True,
])
def test_success_fibonacci(value):
    assert v.fibonacci().validate(value)
    assert v.fibonacci().check(value) is None
    assert v.fibonacci().claim(value) is None


@pytest.mark.parametrize('value', [
    0,
    1346268,
    '',
    None,
    7,
    -1,
    5.2,
    '-1',
    'a',
    ' ',
    '21.0',
    False,
])
def test_fail_fibonacci(value):
    assert v.fibonacci().validate(value) is False

    with pytest.raises(FibonacciException, match=r'must be a valid Fibonacci number'):
        assert v.fibonacci().check(value)
        assert v.fibonacci().claim(value)
