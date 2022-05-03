import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.JsonException import JsonException


@pytest.mark.parametrize('value', [
    '2',
    '"abc"',
    '[1,2,3]',
    '["foo", "bar", "number", 1]',
    '{"foo": "bar", "number":1}',
    '[]',
    '{}',
    'false',
    'null',
])
def test_success_json(value):
    assert v.json().validate(value)
    assert v.json().check(value) is None
    assert v.json().claim(value) is None


@pytest.mark.parametrize('value', [
    False,
    object(),
    [],
    '',
    'a',
    'xx',
    '{foo: bar}',
    '{foo: "baz"}',
])
def test_fail_json(value):
    assert v.json().validate(value) is False

    with pytest.raises(JsonException, match=r' must be a valid JSON string'):
        assert v.json().check(value)
        assert v.json().claim(value)
