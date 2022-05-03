from datetime import datetime

import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.TypeException import TypeException


@pytest.mark.parametrize('val_type, value', [
    ['str', 'alexey'],
    ['int', 123],
    ['list', [123]],
    ['tuple', (123,)],
    ['NoneType', None],
    ['bytes', 'alexey'.encode()],
])
def test_success_type(val_type, value):
    assert v.type(val_type).validate(value)
    assert v.type(val_type).check(value) is None
    assert v.type(val_type).claim(value) is None


@pytest.mark.parametrize('val_type, value', [
    ['str', 123],
    ['int', '123'],
])
def test_fail_type(val_type, value):
    assert v.type(val_type).validate(value) is False

    with pytest.raises(TypeException, match=r' must be '):
        assert v.type(val_type).check(value)
        assert v.type(val_type).claim(value)


@pytest.mark.parametrize('val_type, value', [
    ['datetime.datetime', datetime.now()],
    [None, None],
])
def test_fail_type2(val_type, value):
    with pytest.raises(ComponentException, match=r' is not a valid type '):
        assert v.type(val_type).validate(value)
        assert v.type(val_type).check(value)
        assert v.type(val_type).claim(value)
