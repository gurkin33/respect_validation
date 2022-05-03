import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


def test_success_allOf():
    assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).validate(10)
    assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).claim(10) is None
    assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).check(10) is None


def test_fail_allOf():
    with pytest.raises(ValidationException, match='must be of type integer'):
        assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).check('1000')
        assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).claim('1000')
    assert v.allOf(v.intType(), v.Between(1, 100), v.Max(100)).validate('1000') is False
