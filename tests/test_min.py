from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MinException import MinException


@pytest.mark.parametrize('left, value', [
    [10, 10],
    [10, 11],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2010-01-01', '%Y-%m-%d')],
    ['a', 'b'],
    [100, 165.0],
    [-100, 200],
    [200, 200],
    [200, 300],
    ['a', 'a'],
    ['a', 'c'],
    [datetime.strptime('13-05-2014 03:16', '%d-%m-%Y %H:%M'), datetime.strptime('20-05-2014 03:16', '%d-%m-%Y %H:%M')],
    [50, 50],
    [range(10), 10],
])
def test_success_min(left, value):
    assert v.min(left).validate(value)
    assert v.min(left).check(value) is None
    assert v.min(left).claim(value) is None


@pytest.mark.parametrize('left, value', [
    [10, 9],
    [datetime.strptime('2011-01-01', '%Y-%m-%d'), datetime.strptime('2009-01-01', '%Y-%m-%d')],
    ['C', 'A'],

    [100, ''],
    [100, ''],
    [500, 300],
    [0, -250],
    [0, -50],
    [range(1), 0],
    [2040, datetime.strptime('2018-01-25', '%Y-%m-%d')],
    [10.5, datetime.strptime('2018-01-25', '%Y-%m-%d')],
])
def test_fail_min(left, value):
    assert v.min(left).validate(value) is False

    with pytest.raises(MinException, match=r'must be greater than or equal to'):
        assert v.min(left).check(value)
        assert v.min(left).claim(value)
