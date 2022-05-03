import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.FactorException import FactorException


@pytest.mark.parametrize('factor,value', [
    [1, 1],
    [2, 1],
    [3, 3],
    [4, 2],
    [4, 4],
    [5, 1],
    [5, 5],
    [6, 1],
    [6, 2],
    [0, 0],
    [0, 1],
    [0, 98764321261],
    [-0, 1],
    [-6, 2],
    [-3, 3],
    [-5, 1],
    [-0, 98764321261],
    [-5, -1],
    [-6, -1],
    [-3, -3],
    [-0, -98764321261],
    [4, 2.0],
    [-0, -5.000000],
    [-0, float(-98764321261)],
    [98764321261, True],
])
def test_success_factor(factor, value):
    assert v.factor(factor).validate(value)
    assert v.factor(factor).check(value) is None
    assert v.factor(factor).claim(value) is None


@pytest.mark.parametrize('factor,value', [
    [6, '1'],
    [6, '2'],
    [3, 2],
    [4, 3],
    [5, 2],
    [5, 3],
    [5, 4],
    [1, 0],
    [2, 0],
    [-2, 0],
    [-5, 4],
    [-4, 3],
    [-3, -2],
    [-5, -2],
    [-2, -0],
    [-2, '-0.0000'],
    [-2, 0.00],
    [3, 2.0],
    [5, 2.000000],
    [98764321261, 0.5],
    [98764321261, 1.5],
    [98764321261, -0.5],
    [98764321261, -1.5],
    [98764321261, 'a'],
    [98764321261, 'foo'],
    [98764321261, []],
    [98764321261, object()],
    [98764321261, None],
    [98764321261, False],
])
def test_fail_factor(factor, value):
    assert v.factor(factor).validate(value) is False

    with pytest.raises(FactorException, match=r'must be a factor of '):
        assert v.factor(factor).check(value)
        assert v.factor(factor).claim(value)
