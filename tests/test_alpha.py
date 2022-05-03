import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.AlphaException import AlphaException


@pytest.mark.parametrize(('more_chars', 'value'), [
    (None, 'alganet'),
    ('.', 'google.com'),
    ('0-9', '0alg-anet9'),
    ('!@#$%^&*(){}', '!@#$%^&*(){}'),
    (None, 'dgç'),
    (None, 'русский'),
    (('-', ' '), 'a-b c'),
])
def test_success_alpha(value, more_chars):
    if more_chars:
        assert v.alpha(*more_chars).validate(value)
        assert v.alpha(*more_chars).check(value) is None
        assert v.alpha(*more_chars).claim(value) is None
    else:
        assert v.alpha().validate(value)
        assert v.alpha().check(value) is None
        assert v.alpha().claim(value) is None


@pytest.mark.parametrize(('more_chars', 'value'), [
    (None, ''),
    (None, '@#$'),
    (None, '_'),
    (None, '122al'),
    (None, '122'),
    (None, 11123),
    (None, 0),
    (None, None),
    (None, object()),
    (None, []),
    (None, "\nabc"),
    (None, "\tdef"),
    (None, 'alganet alganet'),
])
def test_fail_alpha(value, more_chars):
    assert v.alpha().validate(value) is False

    with pytest.raises(AlphaException):
        if more_chars:
            assert v.alpha(*more_chars).check(value)
            assert v.alpha(*more_chars).claim(value)
        else:
            assert v.alpha().check(value)
            assert v.alpha().claim(value)
