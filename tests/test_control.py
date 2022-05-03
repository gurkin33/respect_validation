import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ControlException import ControlException


@pytest.mark.parametrize('more_chars, value', [
    [None, "\n"],
    [None, "\r"],
    [None, "\t"],
    [None, "\n\r\t"],
    ['!@#$%^&*(){} ', '!@#$%^&*(){} '],
    ['[]?+=/\\-_|"\',<>. ', "[]?+=/\\-_|\"',<>. \t \n"],
])
def test_success_control(more_chars, value):
    if more_chars:
        assert v.control(more_chars).validate(value)
        assert v.control(more_chars).check(value) is None
        assert v.control(more_chars).claim(value) is None
    else:
        assert v.control().validate(value)
        assert v.control().check(value) is None
        assert v.control().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '16-50',
    'a',
    ' '
    'Foo',
    '12.1',
    '-12',
    -12,
    'alganet',
    [],
    object()
])
def test_fail_control(value):
    assert v.control().validate(value) is False

    with pytest.raises(ControlException, match="must contain only control characters"):
        assert v.control().check(value)
        assert v.control().claim(value)
