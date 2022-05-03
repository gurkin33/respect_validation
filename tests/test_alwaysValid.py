import pytest
import respect_validation.Validator as v


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
def test_fail_alwaysValid(value):
    assert v.alwaysValid().validate(value) is True
    assert v.alwaysValid().check(value) is None
    assert v.alwaysValid().claim(value) is None
