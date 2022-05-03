import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.DecimalException import DecimalException


@pytest.mark.parametrize('count, value', [
    [0, 1],
    [1, 1.0],
    [1, 1.00],
    [1, 1.000],
    [2, '27990.50'],
    [1, 1.1],
    [1, '1.3'],
    [1, 1.50],
    [3, '1.000'],
    [3, 123456789.001],
])
def test_success_decimal(count, value):
    assert v.decimal(count).validate(value)
    assert v.decimal(count).check(value) is None
    assert v.decimal(count).claim(value) is None


@pytest.mark.parametrize('count, value', [
    [1, '1.50'],
    [1, '27990.50'],
    [0, 2.0],
    [0, False],
    [0, True],
    [0, []],
    [0, object()],
])
def test_fail_decimal(count, value):
    assert v.decimal(count).validate(value) is False

    with pytest.raises(DecimalException, match=r'must have \d decimals'):
        assert v.decimal(count).check(value)
        assert v.decimal(count).claim(value)
