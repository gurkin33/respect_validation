import random

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MacAddressException import MacAddressException


@pytest.mark.parametrize('value', [
    '00:11:22:33:44:55',
    '66-77-88-99-aa-bb',
    'AF:0F:bd:12:44:ba',
    '90-bc-d3-1a-dd-cc',
])
def test_success_macAddress(value):
    assert v.macAddress().validate(value)
    assert v.macAddress().check(value) is None
    assert v.macAddress().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '00-1122:33:44:55',
    True,
    ['90-bc-d3-1a-dd-cc'],
    str(''.join(random.choice('0123456789abcdef') for _ in range(12))),
    None
])
def test_fail_macAddress(value):
    assert v.macAddress().validate(value) is False

    with pytest.raises(MacAddressException, match=r' must be a valid MAC address'):
        assert v.macAddress().check(value)
        assert v.macAddress().claim(value)
