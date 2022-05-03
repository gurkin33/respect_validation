import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.RomanException import RomanException


@pytest.mark.parametrize('value', [
    'III',
    'IV',
    'VI',
    'XIX',
    'XLII',
    'LXII',
    'CXLIX',
    'CLIII',
    'MCCXXXIV',
    'MMXXIV',
    'MCMLXXV',
    'MMMMCMXCIX',
])
def test_success_roman(value):
    assert v.roman().validate(value)
    assert v.roman().check(value) is None
    assert v.roman().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    ' ',
    'IIII',
    'IVVVX',
    'CCDC',
    'MXM',
    'XIIIIIIII',
    'MIMIMI',
])
def test_fail_roman(value):
    assert v.roman().validate(value) is False

    with pytest.raises(RomanException, match=r' must be a valid Roman numeral'):
        assert v.roman().check(value)
        assert v.roman().claim(value)
