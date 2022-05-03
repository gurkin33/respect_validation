from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.LessThanException import LessThanException


@pytest.mark.parametrize('left,value', [
    [10, 9],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2000-01-01', '%Y-%m-%d')],
    ['3 days ago', 'today'],
    ['b', 'a'],
    [range(5), 4],
])
def test_success_lessThan(left, value):
    assert v.lessThan(left).validate(value)
    assert v.lessThan(left).check(value) is None
    assert v.lessThan(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    [10, 10],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2020-01-01', '%Y-%m-%d')],
    ['yesterday', 'tomorrow morning'],
    ['a', 'z'],
    [range(5), 6],
    [1900, datetime.strptime('2018-01-25', '%Y-%m-%d')],
    [10.5, datetime.strptime('2018-01-25', '%Y-%m-%d')],
])
def test_fail_lessThan(left, value):
    assert v.lessThan(left).validate(value) is False

    with pytest.raises(LessThanException, match=r' must be less than '):
        assert v.lessThan(left).check(value)
        assert v.lessThan(left).claim(value)
