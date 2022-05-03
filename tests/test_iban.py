import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IbanException import IbanException


@pytest.mark.parametrize('value', [
    'BE71 0961 2345 6769',
    'FR76 3000 6000 0112 3456 7890 189',
    'DE89 3704 0044 0532 0130 00',
    'GR96 0810 0010 0000 0123 4567 890',
    'RO09 BCYP 0000 0012 3456 7890',
    'SA44 2000 0001 2345 6789 1234',
    'ES79 2100 0813 6101 2345 6789',
    'SE35 5000 0000 0549 1000 0003',
    'CH56 0483 5012 3456 7800 9',
    'CH9300762011623852957',
    'GB98 MIDL 0700 9312 3456 78',
])
def test_success_iban(value):
    assert v.iban().validate(value)
    assert v.iban().check(value) is None
    assert v.iban().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    123456789,
    True,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
    '&"\'(-_)@-*/+.',
    'SE35 5000 5880 7742',
    'CH93 5000 5880 7742',
    'HU42 5000 5880 7742',
    'DE89 5000 5880 7742',
])
def test_fail_iban(value):
    assert v.iban().validate(value) is False

    with pytest.raises(IbanException, match=r' must be a valid IBAN'):
        assert v.iban().check(value)
        assert v.iban().claim(value)
