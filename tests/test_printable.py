import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PrintableException import PrintableException


@pytest.mark.parametrize('value', [
    ' ',
    'LKA#@%.54',
    'foobar',
    '16-50',
    '123',
    'foo bar',
    '#$%&*_',
])
def test_success_printable(value):
    assert v.printable().validate(value)
    assert v.printable().check(value) is None
    assert v.printable().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    None,
    'foo' + chr(7) + 'bar',
    'foo' + chr(10) + 'bar',
])
def test_fail_printable(value):
    assert v.printable().validate(value) is False

    with pytest.raises(PrintableException, match=r' must contain only printable characters'):
        assert v.printable().check(value)
        assert v.printable().claim(value)
