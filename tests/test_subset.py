import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.SubsetException import SubsetException


@pytest.mark.parametrize('subset,value', [
    [([],), []],
    [([1],), [1]],
    [([1, 1],), [1]],
    [([1],), [1, 1]],
    [([2, 1, 3],), [1, 2]],
    [([1, 2, 3],), [1, 2]],
    [(['a', 1, 2],), [1]],
])
def test_success_subset(subset, value):
    assert v.subset(*subset).validate(value)
    assert v.subset(*subset).check(value) is None
    assert v.subset(*subset).claim(value) is None


@pytest.mark.parametrize('subset, value', [
    [([],), [1]],
    [([1],), [2]],
    [([1, 2],), [1, 2, 3]],
    [(['a', 'b'],), ['c']],
])
def test_fail_subset(subset, value):
    assert v.subset(*subset).validate(value) is False

    with pytest.raises(SubsetException, match=r' must be subset of'):
        assert v.subset(*subset).check(value)
        assert v.subset(*subset).claim(value)
