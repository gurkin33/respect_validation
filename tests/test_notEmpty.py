import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NotEmptyException import NotEmptyException


@pytest.mark.parametrize('value', [
    1,
    ' oi',
    [5],
    [0],
    object(),
])
def test_success_notEmpty(value):
    assert v.notEmpty().validate(value)
    assert v.notEmpty().check(value) is None
    assert v.notEmpty().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '    ',
    "\n",
    False,
    None,
    [],
])
def test_fail_notEmpty(value):
    assert v.notEmpty().validate(value) is False

    with pytest.raises(NotEmptyException, match=r' must not be empty'):
        assert v.notEmpty().check(value)
        assert v.notEmpty().claim(value)
