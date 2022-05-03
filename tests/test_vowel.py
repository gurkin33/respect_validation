import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.VowelException import VowelException


@pytest.mark.parametrize('value', [
    'a',
    'e',
    'i',
    'o',
    'u',
    'aeiou',
    'uoiea',
])
def test_success_vowel(value):
    assert v.vowel().validate(value)
    assert v.vowel().check(value) is None
    assert v.vowel().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    ' ',
    "\n",
    "\t",
    "\r",
    None,
    '16',
    'F',
    'g',
    'Foo',
    -50,
    'basic',
])
def test_fail_vowel(value):
    assert v.vowel().validate(value) is False

    with pytest.raises(VowelException, match=r' must contain only vowels'):
        assert v.vowel().check(value)
        assert v.vowel().claim(value)
