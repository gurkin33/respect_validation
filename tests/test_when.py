import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


@pytest.mark.parametrize('value', [
    2,
    'alexey'
])
def test_success_when(value):
    assert v.when(v.IntType(), v.Between(1, 100), v.Length(3, 6)).validate(value)
    assert v.when(v.IntType(), v.Between(1, 100), v.Length(3, 6)).check(value) is None
    assert v.when(v.IntType(), v.Between(1, 100), v.Length(3, 6)).claim(value) is None


@pytest.mark.parametrize('value', [
    101,
    '10',
    'Alexey Mochalin',
    None,
    False,
    []
])
def test_fail_when(value):
    assert v.when(v.IntType(), v.Between(1, 100), v.Length(5, 6)).validate(value) is False

    with pytest.raises(ValidationException, match=r'(must have a length between|must be between )'):
        assert v.when(v.IntType(), v.Between(1, 100), v.Length(5, 6)).check(value)
        assert v.when(v.IntType(), v.Between(1, 100), v.Length(5, 6)).claim(value)
