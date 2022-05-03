import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.TrueValException import TrueValException


@pytest.mark.parametrize('value', [
    True,
    1,
    '1',
    'true',
    'on',
    'yes',
    'TRUE',
    'ON',
    'YES',
    'True',
    'On',
    'Yes',
])
def test_success_trueVal(value):
    assert v.trueVal().validate(value)
    assert v.trueVal().check(value) is None
    assert v.trueVal().claim(value) is None


@pytest.mark.parametrize('value', [
    False,
    0,
    0.5,
    2,
    '0',
    'false',
    'off',
    'no',
    'truth',
])
def test_fail_trueVal(value):
    assert v.trueVal().validate(value) is False

    with pytest.raises(TrueValException, match=r' is not considered as "True"'):
        assert v.trueVal().check(value)
        assert v.trueVal().claim(value)
