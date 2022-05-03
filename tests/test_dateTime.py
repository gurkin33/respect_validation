from datetime import datetime
import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DateTimeException import DateTimeException


@pytest.mark.parametrize('date_format, value', [
    ['%Y-%m-%d', '2009-09-09'],
    ['%d/%m/%Y', '23/05/1987'],
    ['%Y-%m-%dT%H:%M:%S.%f', '2004-02-12T15:19:21.000001'],
    ['%c', 'Tue Aug 16 21:30:00 1988'],
    ['%I', '06'],
    ['%Y%m', '202302'],
    [None, '2009-09-09'],
    [None, '2011-11-04T00:05:23'],
    [None, datetime.fromtimestamp(1657598400)],
])
def test_success_dateTime(date_format, value):
    if date_format:
        assert v.dateTime(date_format).validate(value)
        assert v.dateTime(date_format).check(value) is None
        assert v.dateTime(date_format).claim(value) is None
    else:
        assert v.dateTime().validate(value)
        assert v.dateTime().check(value) is None
        assert v.dateTime().claim(value) is None


@pytest.mark.parametrize('date_format, value', [
    [None, 'not-a-date'],
    [None, []],
    [None, True],
    [None, False],
    [None, None],
    [None, ''],
    ['%Y-%m-%d', '2009-12-00'],
    ['%Y-%m-%d', '2018-02-29'],
    ['h', 24],
])
def test_fail_dateTime(date_format, value):
    if date_format:
        assert v.dateTime(date_format).validate(value) is False
        with pytest.raises(DateTimeException, match="must be a valid date/time"):
            assert v.dateTime(date_format).check(value)
            assert v.dateTime(date_format).claim(value)
    else:
        assert v.dateTime().validate(value) is False
        with pytest.raises(DateTimeException, match="must be a valid date/time"):
            assert v.dateTime().check(value)
            assert v.dateTime().claim(value)
