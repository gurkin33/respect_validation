import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NumericValException import NumericValException


@pytest.mark.parametrize('value', [
    164,
    165.0,
    -165,
    '165',
    '165.0',
    '+165.0',
])
def test_success_numericVal(value):
    assert v.numericVal().validate(value)
    assert v.numericVal().check(value) is None
    assert v.numericVal().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    None,
    'a',
    ' ',
    'Foo',
])
def test_fail_numericVal(value):
    assert v.numericVal().validate(value) is False

    with pytest.raises(NumericValException, match=r' must be numeric'):
        assert v.numericVal().check(value)
        assert v.numericVal().claim(value)
