import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.BoolTypeException import BoolTypeException


@pytest.mark.parametrize('value', [
    True,
    False
])
def test_success_boolType(value):
    assert v.boolType().validate(value)
    assert v.boolType().check(value) is None
    assert v.boolType().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    'foo',
    123123,
    object(),
    [],
    1,
    0,
    None,
])
def test_fail_boolType(value):
    assert v.boolType().validate(value) is False

    with pytest.raises(BoolTypeException, match="must be of type boolean"):
        assert v.boolType().check(value)
        assert v.boolType().claim(value)
