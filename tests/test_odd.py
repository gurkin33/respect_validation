import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.OddException import OddException


@pytest.mark.parametrize('value', [
    -5,
    -1,
    1,
    13,
    True,
])
def test_success_odd(value):
    assert v.odd().validate(value)
    assert v.odd().check(value) is None
    assert v.odd().claim(value) is None


@pytest.mark.parametrize('value', [
     [],
     object(),
     False,
     '',
     -2,
     -0,
     0,
     32,
])
def test_fail_odd(value):
    assert v.odd().validate(value) is False

    with pytest.raises(OddException, match=r' must be an odd number'):
        assert v.odd().check(value)
        assert v.odd().claim(value)
