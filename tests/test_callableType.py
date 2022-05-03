import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.CallableTypeException import CallableTypeException


@pytest.mark.parametrize('value', [
    'alex'.encode,
    'viktor'.upper,
    list,
    len,
    v
])
def test_success_callableType(value):
    assert v.callableType().validate(value)
    assert v.callableType().check(value) is None
    assert v.callableType().claim(value) is None


@pytest.mark.parametrize('value', [
    ' ',
    'alex'.encode(),
    [],
    object(),
    None,
])
def test_fail_callableType(value):
    assert v.callableType().validate(value) is False

    with pytest.raises(CallableTypeException, match="must be callable"):
        assert v.callableType().check(value)
        assert v.callableType().claim(value)
