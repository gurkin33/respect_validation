import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.PeselException import PeselException


@pytest.mark.parametrize('value', [
    0x4EADCD168,  # 0x4EADCD168 === 21120209256
    49040501580,
    '49040501580',
    '39012110375',
    '50083014540',
    '69090515504',
    '21120209256',
    '01320613891',
])
def test_success_pesel(value):
    assert v.pesel().validate(value)
    assert v.pesel().check(value) is None
    assert v.pesel().claim(value) is None


@pytest.mark.parametrize('value', [
    '1',
    '22',
    'PESEL',
    '0x4EADCD168',
    'PESEL123456',
    '690905155.4',
    '21120209251',
    '21120209250',
    '01320613890',
])
def test_fail_pesel(value):
    assert v.pesel().validate(value) is False

    with pytest.raises(PeselException, match=r' must be a valid PESEL'):
        assert v.pesel().check(value)
        assert v.pesel().claim(value)
