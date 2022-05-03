import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IntTypeException import IntTypeException


@pytest.mark.parametrize('value', [
    0,
    123456,
    True
])
def test_success_intType(value):
    assert v.intType().validate(value)
    assert v.intType().check(value) is None
    assert v.intType().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    None,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
])
def test_fail_intType(value):
    assert v.intType().validate(value) is False

    with pytest.raises(IntTypeException, match=r' must be of type integer'):
        assert v.intType().check(value)
        assert v.intType().claim(value)
