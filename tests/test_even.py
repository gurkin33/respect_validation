import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.EvenException import EvenException


@pytest.mark.parametrize('value', [
    2,
    -2,
    0,
    32,
])
def test_success_even(value):
    assert v.even().validate(value)
    assert v.even().check(value) is None
    assert v.even().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    2.2,
    -5,
    -1,
    1,
    13
])
def test_fail_even(value):
    assert v.even().validate(value) is False

    with pytest.raises(EvenException, match=" must be an even number"):
        assert v.even().check(value)
        assert v.even().claim(value)
