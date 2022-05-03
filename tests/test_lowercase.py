import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LowercaseException import LowercaseException


@pytest.mark.parametrize('value', [
    'lowercase',
    'lowercase-with-dashes',
    'lowercase with spaces',
    'lowercase with numbers 123',
    'lowercase with specials characters like ã ç ê',
    'with specials characters like # $ % & * +',
    'τάχιστη αλώπηξ βαφής ψημένη γη, δρασκελίζει υπέρ νωθρού κυνός',
    'a42',
    'a!@#$%^',
])
def test_success_lowercase(value):
    assert v.lowercase().validate(value)
    assert v.lowercase().check(value) is None
    assert v.lowercase().claim(value) is None


@pytest.mark.parametrize('value', [
    42,
    [],
    object(),
    'UPPERCASE',
    'CamelCase',
    'First Character Uppercase',
    'With Numbers 1 2 3',
    '42',
    '!@#$%^',
    ''
])
def test_fail_lowercase(value):
    assert v.lowercase().validate(value) is False

    with pytest.raises(LowercaseException, match=r' must be lowercase'):
        assert v.lowercase().check(value)
        assert v.lowercase().claim(value)
