import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ValidationException


def test_success_noWhitespace():
    assert v.Not(v.noWhitespace()).validate('     ')
    assert v.Not(v.noWhitespace()).check('     ') is None
    assert v.Not(v.noWhitespace()).claim('     ') is None

    assert v.Not(v.noWhitespace().digit()).validate('12 34')
    assert v.Not(v.noWhitespace().digit()).check('12 34') is None
    assert v.Not(v.noWhitespace().digit()).claim('12 34') is None

    assert v.Not(v.numericVal().intVal()).validate(66.6)
    assert v.Not(v.numericVal().intVal()).check(66.6) is None
    assert v.Not(v.numericVal().intVal()).claim(66.6) is None


def test_fail_noWhitespace():
    assert v.Not(v.noWhitespace()).validate('Something') is False

    with pytest.raises(ValidationException, match=r'must not be of type string'):
        assert v.Not(v.noWhitespace().stringType()).check('Something')
        assert v.Not(v.noWhitespace().stringType()).claim('Something')
