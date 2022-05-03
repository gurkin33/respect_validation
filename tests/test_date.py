from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.DateException import DateException


@pytest.mark.parametrize('date_format,value', [
    [None, '2017-12-31'],
    ['%m/%d/%y', '12/31/17'],
    ['%b %d, %Y', 'May 1, 2017'],
    [None, '2020-02-29'],
    [None, datetime.now()],
])
def test_success_date(date_format, value):
    if date_format:
        assert v.date(date_format).validate(value)
        assert v.date(date_format).check(value) is None
        assert v.date(date_format).claim(value) is None
    else:
        assert v.date().validate(value)
        assert v.date().check(value) is None
        assert v.date().claim(value) is None


@pytest.mark.parametrize('date_format,value', [
    ['%Y%d%m', 20173112],
    [None, 'not-a-date'],
    [None, []],
    [None, True],
    [None, False],
    [None, None],
    [None, ''],
    [None, '1988-02-30'],
    ['%d/%m/%y', '12/31/17'],
    [None, '2019-02-29'],
    [None, ''],
    ['%Y-%m-%d', '2009-12-00'],
    ['%Y-%m-%d', '2018-02-29'],
    [None, '2014-99'],
    ['%d', 1],
    ['%Y-%m', '2014-99'],
    ['%m', '99'],
])
def test_fail_date(date_format, value):
    if date_format:
        assert v.date(date_format).validate(value) is False
        with pytest.raises(DateException, match="must be a valid date in the format"):
            assert v.date(date_format).check(value)
            assert v.date(date_format).claim(value)
    else:
        assert v.date().validate(value) is False
        with pytest.raises(DateException, match="must be a valid date in the format"):
            assert v.date().check(value)
            assert v.date().claim(value)


def test_fail_date2():
    with pytest.raises(ComponentException, match="is not a valid date format"):
        assert v.date(123123).validate('value') is False
        assert v.date(123123).check('value')
        assert v.date(123123).claim('value')
