import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NotOptionalException import NotOptionalException


@pytest.mark.parametrize('value', [
    [],
    ' ',
    0,
    '0',
    0,
    '0.0',
    False,
    [''],
    [' '],
    [0],
    ['0'],
    [False],
    ['', [0]],
    object(),
])
def test_success_notOptional(value):
    assert v.notOptional().validate(value)
    assert v.notOptional().check(value) is None
    assert v.notOptional().claim(value) is None


@pytest.mark.parametrize('value', [
    None,
    '',
])
def test_fail_notOptional(value):
    assert v.notOptional().validate(value) is False

    with pytest.raises(NotOptionalException, match=r' must not be optional'):
        assert v.notOptional().check(value)
        assert v.notOptional().claim(value)
