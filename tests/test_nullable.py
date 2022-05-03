import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MinException import MinException


@pytest.mark.parametrize('value', [
    1,
    '1',
    None
])
def test_success_nullable(value):
    assert v.nullable(v.digit()).validate(value)
    assert v.nullable(v.digit()).check(value) is None
    assert v.nullable(v.digit()).claim(value) is None


@pytest.mark.parametrize('value', [
    1,
    '1',
])
def test_fail_nullable(value):
    assert v.nullable(v.min(10)).validate(value) is False

    with pytest.raises(MinException, match=r' must be greater than or equal to 10'):
        assert v.nullable(v.min(10)).check(value)
        assert v.nullable(v.min(10)).claim(value)
