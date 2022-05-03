import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


@pytest.mark.parametrize(('rules', 'value'), [
    [(v.intType(), v.stringType(), v.NoneType()), 10],
    [(v.intType(), v.stringType(), v.NoneType()), '10'],
    [(v.intType(), v.stringType(), v.NoneType()), None],
])
def test_success_anyOf(rules, value):
    assert v.anyOf(*rules).validate(value)
    assert v.anyOf(*rules).claim(value) is None
    assert v.anyOf(*rules).check(value) is None


@pytest.mark.parametrize(('rules', 'value'), [
    [(v.intType(), v.stringType(), v.Max(200)), None],
])
def test_fail_anyOf(rules, value):
    with pytest.raises(ValidationException, match='At least one of these rules must pass for'):
        assert v.anyOf(*rules).check(value)
        assert v.anyOf(*rules).claim(value)
    assert v.anyOf(*rules).validate(value) is False
