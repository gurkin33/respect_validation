import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.MultipleException import MultipleException


@pytest.mark.parametrize('left, value', [
    [5, 20],
    [5, 5],
    [5, 0],
    [5, -500],
    [1, 0],
    [1, 1],
    [1, 2],
    [1, 3],
    [0, 0],  # Only 0 is multiple of 0
])
def test_success_multiple(left, value):
    assert v.multiple(left).validate(value)
    assert v.multiple(left).check(value) is None
    assert v.multiple(left).claim(value) is None


@pytest.mark.parametrize('left, value', [
    [5, 11],
    [5, 3],
    [5, -1],
    [3, 4],
    [10, -8],
    [10, 57],
    [10, 21],
    [0, 1],
    [0, 2],
])
def test_fail_multiple(left, value):
    assert v.multiple(left).validate(value) is False

    with pytest.raises(MultipleException, match=r' must be multiple of '):
        assert v.multiple(left).check(value)
        assert v.multiple(left).claim(value)
