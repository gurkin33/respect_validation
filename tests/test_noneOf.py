import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.NoneOfException import NoneOfException


@pytest.mark.parametrize('value', [
    '',
    None,
    0,
    'wpoiur',
    'Foo',
    []
])
def test_success_noneOf(value):
    assert v.noneOf(v.negative(), v.between(100, 200)).validate(value)
    assert v.noneOf(v.negative(), v.between(100, 200)).check(value) is None
    assert v.noneOf(v.negative(), v.between(100, 200)).claim(value) is None


@pytest.mark.parametrize('value', [
    [1, 2],
    {'name': '123123'},
    ' a',
    -5,
])
def test_fail_noneOf(value):
    assert v.noneOf(v.negative(), v.between(-100, 200)).validate(value) is False

    with pytest.raises(NoneOfException, match=r'None of these rules must pass for'):
        assert v.noneOf(v.negative(), v.between(-100, 200)).check(value) is None
        assert v.noneOf(v.negative(), v.between(-100, 200)).claim(value) is None
