import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


@pytest.mark.parametrize('condition, value', [
    [('foo', 'equals', 'bar'), {"foo": 42, "bar": 42}],
    [('password', 'include', 'valid_passwords'),
     {"password": "shuberry", "password_confirmation": "shuberry", "valid_passwords": ["shuberry", "monty-python"]}],
    [('password', 'equals', 'password_confirmation'),
     {"password": "shuberry", "password_confirmation": "shuberry", "valid_passwords": ["shuberry", "monty-python"]}]
])
def test_success_keyValue(condition, value):
    assert v.keyValue(*condition).validate(value)
    assert v.keyValue(*condition).check(value) is None
    assert v.keyValue(*condition).claim(value) is None


@pytest.mark.parametrize('condition, value', [
    [('foo', 'equals', 'bar'), {'foo': 43, 'bar': 42}],
    [('foo', 'equals', 'bar'), {'bar': 42}],
    [('foo', 'equals', 'bar'), {'foo': True}],
    [('foo', 'probably_not_a_rule', 'bar'), {'foo': True, 'bar': False}],
])
def test_fail_keyValue(condition, value):
    assert v.keyValue(*condition).validate(value) is False

    with pytest.raises(ValidationException, match=r'(must be present|foo must be equal to bar|bar must be valid to validate foo)'):
        assert v.keyValue(*condition).check(value)
        assert v.keyValue(*condition).claim(value)
