import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.InstanceException import InstanceException


@pytest.mark.parametrize('left,value', [
    ['str', 'aaaaa'],
    ['int', 123123],
    ['range', range(23)],
    ['dict', {'hello': 'world'}],
])
def test_success_instance(left, value):
    assert v.instance(left).validate(value)
    assert v.instance(left).check(value) is None
    assert v.instance(left).claim(value) is None


@pytest.mark.parametrize('left,value', [
    ['int', '123'],
    ['bool', 23],
    ['str', 23],
    ['object', '123123'],
])
def test_fail_instance(left, value):
    assert v.instance(left).validate(value) is False

    with pytest.raises(InstanceException, match=r' must be an instance of '):
        assert v.instance(left).check(value)
        assert v.instance(left).claim(value)
