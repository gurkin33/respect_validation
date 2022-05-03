from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.TimeException import TimeException


@pytest.mark.parametrize('date_format,value', [
    [None, '00:00:00'],
    [None, '23:20:59'],
    ['%H:%M', '23:59'],
    [None, datetime.now()],
    ['%H:%M', datetime.now()],
])
def test_success_time(date_format, value):
    if date_format:
        assert v.time(date_format).validate(value)
        assert v.time(date_format).check(value) is None
        assert v.time(date_format).claim(value) is None
    else:
        assert v.time().validate(value)
        assert v.time().check(value) is None
        assert v.time().claim(value) is None


@pytest.mark.parametrize('date_format,value', [
    [None, 'not-a-time'],
    [None, []],
    [None, True],
    [None, False],
    [None, None],
    [None, ''],
    [None, '00:00:60'],
])
def test_fail_time(date_format, value):
    if date_format:
        assert v.time(date_format).validate(value) is False
        with pytest.raises(TimeException, match="must be a valid time in the format"):
            assert v.time(date_format).check(value)
            assert v.time(date_format).claim(value)
    else:
        assert v.time().validate(value) is False
        with pytest.raises(TimeException, match="must be a valid time in the format"):
            assert v.time().check(value)
            assert v.time().claim(value)


def test_fail_time2():
    with pytest.raises(ComponentException, match="is not a valid date format"):
        assert v.time(123123).validate('value') is False
        assert v.time(123123).check('value')
        assert v.time(123123).claim('value')
