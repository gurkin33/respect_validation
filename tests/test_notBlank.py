import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NotBlankException import NotBlankException


@pytest.mark.parametrize('value', [
    1,
    ' oi',
    [5],
    [1],
])
def test_success_notBlank(value):
    assert v.notBlank().validate(value)
    assert v.notBlank().check(value) is None
    assert v.notBlank().claim(value) is None


@pytest.mark.parametrize('value', [
    None,
    '',
    [],
    ' ',
    0,
    '0',
    0,
    False,
    [''],
    [0],
    ['0'],
    [False],
    object(),
])
def test_fail_notBlank(value):
    assert v.notBlank().validate(value) is False

    with pytest.raises(NotBlankException, match=r' must not be blank'):
        assert v.notBlank().check(value)
        assert v.notBlank().claim(value)
