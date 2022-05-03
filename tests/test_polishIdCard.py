import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PolishIdCardException import PolishIdCardException


@pytest.mark.parametrize('value', [
    'APH505567',
    'AYE205410',
    'AYW036733',
])
def test_success_polishIdCard(value):
    assert v.polishIdCard().validate(value)
    assert v.polishIdCard().check(value) is None
    assert v.polishIdCard().claim(value) is None


@pytest.mark.parametrize('value', [
    'AAAAAAAAA',
    'APH 505567',
    'AYE205411',
    'AYW036731',
])
def test_fail_polishIdCard(value):
    assert v.polishIdCard().validate(value) is False

    with pytest.raises(PolishIdCardException, match=r' must be a valid Polish Identity Card number'):
        assert v.polishIdCard().check(value)
        assert v.polishIdCard().claim(value)
