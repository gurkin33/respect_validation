from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MaxException import MaxException


@pytest.mark.parametrize('left, value', [
    [10, 9],
    [10, 10],
    [datetime.strptime('2010-01-01', '%Y-%m-%d'), datetime.strptime('2000-01-01', '%Y-%m-%d')],
    ['THIS TEXT IS GREATER than right one', 'IT IS TEXT'],
    ['z', 'a'],
])
def test_success_max(left, value):
    assert v.max(left).validate(value)
    assert v.max(left).check(value) is None
    assert v.max(left).claim(value) is None


@pytest.mark.parametrize('left, value', [
    [10, 11],
    ['TEXT IS Less than right one', 'I AM right side text. Can you see me?'],
    ['B', 'C'],
    [range(3), 4],
    [1900, datetime.strptime('2018-01-25', '%Y-%m-%d')],
    [10.5, datetime.strptime('2018-01-25', '%Y-%m-%d')],
])
def test_fail_max(left, value):
    assert v.max(left).validate(value) is False

    with pytest.raises(MaxException, match=r' must be less than or equal'):
        assert v.max(left).check(value)
        assert v.max(left).claim(value)
