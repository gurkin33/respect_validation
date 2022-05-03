import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.BsnException import BsnException


@pytest.mark.parametrize('value', [
    '612890053',
    '087880532',
    '386625918',
    '601608021',
    '254650703',
    '478063441',
    '478063441',
    '187368429',
    '541777348',
    '254283883',
])
def test_success_bsn(value):
    assert v.bsn().validate(value)
    assert v.bsn().check(value) is None
    assert v.bsn().claim(value) is None


@pytest.mark.parametrize('value', [
    '1234567890',
    '0987654321',
    '13579024',
    '612890054',
    '854650703',
    '283958721',
    '231859081',
    '189023323',
    '238150912',
    '382409678',
    '38240.678',
    '38240a678',
    'abcdefghi',
])
def test_fail_bsn(value):
    assert v.bsn().validate(value) is False

    with pytest.raises(BsnException, match="must be a BSN"):
        assert v.bsn().check(value)
        assert v.bsn().claim(value)
