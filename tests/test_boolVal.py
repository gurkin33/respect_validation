import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.BoolValException import BoolValException


@pytest.mark.parametrize('value', [
    True,
    1,
    'on',
    'yes',
    0,
    False,
    'off',
    'no '
])
def test_success_boolVal(value):
    assert v.boolVal().validate(value)
    assert v.boolVal().check(value) is None
    assert v.boolVal().claim(value) is None


@pytest.mark.parametrize('value', [
    'ok',
    'yep',
    10,
    None,
    '',
])
def test_fail_boolVal(value):
    assert v.boolVal().validate(value) is False

    with pytest.raises(BoolValException, match="must be a boolean value"):
        assert v.boolVal().check(value)
        assert v.boolVal().claim(value)
