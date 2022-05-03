from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LeapDateException import LeapDateException


@pytest.mark.parametrize('date_format, value', [
    ['%Y-%m-%d', '1988-02-29'],
    ['%Y-%m-%d', '1992-02-29'],
    ['%Y-%m-%d', datetime.strptime('1988-02-29', '%Y-%m-%d')],
    ['%Y-%m-%d', datetime.strptime('1992-02-29', '%Y-%m-%d')],
])
def test_success_leapDate(date_format, value):
    assert v.leapDate(date_format).validate(value)
    assert v.leapDate(date_format).check(value) is None
    assert v.leapDate(date_format).claim(value) is None


@pytest.mark.parametrize('date_format,value', [
    ['%Y-%m-%d', '1989-02-29'],
    ['%Y-%m-%d', '1993-02-29'],
    ['%Y-%m-%d', datetime.strptime('1989-07-29', '%Y-%m-%d')],
    ['%Y-%m-%d', datetime.strptime('1993-09-29', '%Y-%m-%d')],
    ['%Y-%m-%d', []],
])
def test_fail_leapDate(date_format, value):
    assert v.leapDate(date_format).validate(value) is False

    with pytest.raises(LeapDateException, match=r' must be leap date'):
        assert v.leapDate(date_format).check(value)
        assert v.leapDate(date_format).claim(value)
