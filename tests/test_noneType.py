import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NoneTypeException import NoneTypeException


@pytest.mark.parametrize('value', [
    None
])
def test_success_noneType(value):
    assert v.noneType().validate(value)
    assert v.noneType().check(value) is None
    assert v.noneType().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    False,
    [],
    0,
    'w poiur',
])
def test_fail_noneType(value):
    assert v.noneType().validate(value) is False

    with pytest.raises(NoneTypeException, match=r' must be None type'):
        assert v.noneType().check(value)
        assert v.noneType().claim(value)
