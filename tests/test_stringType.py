import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.StringTypeException import StringTypeException


@pytest.mark.parametrize('value', [
    '',
    '123123'
])
def test_success_stringType(value):
    assert v.stringType().validate(value)
    assert v.stringType().check(value) is None
    assert v.stringType().claim(value) is None


@pytest.mark.parametrize('value', [
    None,
    [],
    123,
    object()
])
def test_fail_stringType(value):
    assert v.stringType().validate(value) is False

    with pytest.raises(StringTypeException, match=r' must be of type string'):
        assert v.stringType().check(value)
        assert v.stringType().claim(value)
