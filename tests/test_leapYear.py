from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LeapYearException import LeapYearException


@pytest.mark.parametrize('value', [
    '2008',
    2008,
    datetime.strptime('2008-02-29', '%Y-%m-%d'),
])
def test_success_leapYear(value):
    assert v.leapYear().validate(value)
    assert v.leapYear().check(value) is None
    assert v.leapYear().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    '2009',
    '2008-02-29',
    '2009-02-29',
    2009,
    datetime.strptime('2009-07-29', '%Y-%m-%d'),
    [],
])
def test_fail_leapYear(value):
    assert v.leapYear().validate(value) is False

    with pytest.raises(LeapYearException, match=r' must be a leap year'):
        assert v.leapYear().check(value)
        assert v.leapYear().claim(value)
