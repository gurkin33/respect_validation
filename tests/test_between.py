import pytest
from datetime import datetime, timedelta

import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.BetweenException import BetweenException


@pytest.mark.parametrize('min_value, max_value, value', [
    [0, 1, 1],
    [0, 1, 0],
    [10, 20, 15],
    [10, 20, 20],
    [-10, 20, -5],
    [-10, 20, 0],
    ['a', 'z', 'j'],
    [(datetime.today() - timedelta(days=1)), (datetime.today() + timedelta(days=1)), datetime.today()],
    [datetime.strptime('2022-01-01', '%Y-%m-%d'), datetime.strptime('2022-03-01', '%Y-%m-%d'), datetime.strptime('2022-02-04', '%Y-%m-%d')],
    [
        datetime.strptime('2022-01-01 00:00:01', '%Y-%m-%d %H:%M:%S'),
        datetime.strptime('2022-03-01 02:02:01', '%Y-%m-%d %H:%M:%S'),
        datetime.strptime('2022-02-04 02:02:01', '%Y-%m-%d %H:%M:%S')],
    [[1, 2, 3], [2, 3, 4, 5, 6], [2, 5, 5, 5]],
])
def test_success_between(min_value, max_value, value):
    assert v.between(min_value, max_value).validate(value)
    assert v.between(min_value, max_value).check(value) is None
    assert v.between(min_value, max_value).claim(value) is None


@pytest.mark.parametrize('min_value, max_value, value', [
            [10, 20, ''],
            [10, 20, ''],
            [0, 1, 2],
            [0, 1, -1],
            [10, 20, 999],
            [-10, 20, -11],
            ['a', 'j', 'z'],
            [(datetime.today() - timedelta(days=1)), datetime.today(), (datetime.today() + timedelta(days=1))],
            [[1, 2, 3, 4], [2, 3, 4, 5, 6], 11],
])
def test_fail_between(min_value, max_value, value):
    assert v.between(min_value, max_value).validate(value) is False

    with pytest.raises(BetweenException, match="must be between .* and"):
        assert v.between(min_value, max_value).check(value)
        assert v.between(min_value, max_value).claim(value)


def test_fail_between_min_gt_max1():

    with pytest.raises(ComponentException, match="Minimum value cannot be more than or equals to maximum"):
        assert v.between(10, 5).validate(7) is False
        assert v.between(10, 5).check(7)
        assert v.between(10, 5).claim(7)


def test_fail_between_min_gt_max2():

    with pytest.raises(ComponentException, match="Minimum value cannot be more than or equals to maximum"):
        assert v.between(5, 5).validate(7) is False
        assert v.between(5, 5).check(7)
        assert v.between(5, 5).claim(7)


def test_fail_between_min_gt_max3():
    today = datetime.today()
    with pytest.raises(ComponentException, match="Minimum value cannot be more than or equals to maximum"):
        assert v.between(today, today).validate(today) is False
        assert v.between(today, today).check(today)
        assert v.between(today, today).claim(today)
