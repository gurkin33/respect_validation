from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.GreaterThanException import GreaterThanException


@pytest.mark.parametrize('left,value', [
    [10, 11],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2020-01-01', '%Y-%m-%d')],
    ['A', 'B'],
    [range(3), 4],
    [[1, 2, 3], 4],
])
def test_success_greaterThan(left, value):
    assert v.greaterThan(left).validate(value)
    assert v.greaterThan(left).check(value) is None
    assert v.greaterThan(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    [10, 9],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2000-01-01', '%Y-%m-%d')],
    ['yesterday', 'now'],
    ['c', 'a'],
    [range(3), 3],
    [1900, datetime.strptime('2018-01-25', '%Y-%m-%d')],
    [10.5, datetime.strptime('2018-01-25', '%Y-%m-%d')],
])
def test_fail_greaterThan(left, value):
    assert v.greaterThan(left).validate(value) is False

    with pytest.raises(GreaterThanException, match=r' must be greater than '):
        assert v.greaterThan(left).check(value)
        assert v.greaterThan(left).claim(value)
