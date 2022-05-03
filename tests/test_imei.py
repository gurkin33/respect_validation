import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.ImeiException import ImeiException


@pytest.mark.parametrize('value', [
    '35-007752-323751-3',
    '35-209900-176148-1',
    '350077523237513',
    '356938035643809',
    '490154203237518',
    350077523237513,
    356938035643809,
    490154203237518,
])
def test_success_imei(value):
    assert v.imei().validate(value)
    assert v.imei().check(value) is None
    assert v.imei().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    None,
    1.0,
    object(),
    '490154203237512',
    '4901542032375125',
    'Whateveeeeeerrr',
    True,
])
def test_fail_imei(value):
    assert v.imei().validate(value) is False

    with pytest.raises(ImeiException, match=r' must be a valid IMEI'):
        assert v.imei().check(value)
        assert v.imei().claim(value)
