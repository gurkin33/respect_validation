import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.AlwaysInvalidException import AlwaysInvalidException


@pytest.mark.parametrize('value', [
    (0,),
    (1,),
    ('string', ),
    (True, ),
    (False, ),
    (None, ),
    ('', ),
    (list(), ),
    (['array_full'], ),
])
def test_failed_alwaysInvalid(value):
    with pytest.raises(AlwaysInvalidException, match="is always invalid"):
        assert v.alwaysInvalid().validate(value) is False
        assert v.alwaysInvalid().check(value) is None
        assert v.alwaysInvalid().claim(value) is None
