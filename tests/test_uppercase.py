import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.UppercaseException import UppercaseException


@pytest.mark.parametrize('value', [
    '',
    'UPPERCASE',
    'UPPERCASE-WITH-DASHES',
    'UPPERCASE WITH SPACES',
    'UPPERCASE WITH NUMBERS 123',
    'UPPERCASE WITH SPECIALS CHARACTERS LIKE Ã Ç Ê',
    'WITH SPECIALS CHARACTERS LIKE # $ % & * +',
    'ΤΆΧΙΣΤΗ ΑΛΏΠΗΞ ΒΑΦΉΣ ΨΗΜΈΝΗ ΓΗ, ΔΡΑΣΚΕΛΊΖΕΙ ΥΠΈΡ ΝΩΘΡΟΎ ΚΥΝΌΣ',
    # Uppercase should not restrict these
    '42',
    '!@#$%^',
])
def test_success_uppercase(value):
    assert v.uppercase().validate(value)
    assert v.uppercase().check(value) is None
    assert v.uppercase().claim(value) is None


@pytest.mark.parametrize('value', [
    42,
    [],
    object(),
    'lowercase',
    'CamelCase',
    'First Character Uppercase',
    'With Numbers 1 2 3',
])
def test_fail_uppercase(value):
    assert v.uppercase().validate(value) is False

    with pytest.raises(UppercaseException, match=r' must be uppercase'):
        assert v.uppercase().check(value)
        assert v.uppercase().claim(value)
