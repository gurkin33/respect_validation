import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.AlnumException import AlnumException


@pytest.mark.parametrize(('more_chars', 'value'), [
    (None, 'alganet'),
    ('- ! :', 'foo :- 123 !'),
    ('0-9', '0alg-anet0'),
    (None, '1'),
    (None, 'a'),
    (None, 'foobar'),
    (None, 'русский'),
    (None, 'dgç'),
    ('_', 'rubinho_'),
    ('.', 'google.com'),
    (' ', 'alganet alganet'),
    (None, 0),
    ('!@#$%^&*(){}', '!@#$%^&*(){}abc123'),
    ('[]?+=/\\-_|"\',<>.', '[]?+=/\\-_|"\',<>.abc123'),
    ("[]?+=/\\-_|\"',<>. \t\n", "abc[]?+=/\\-_|\"',<>. \t\n123"),
    (('-', '*'), 'a-1*d'),
])
def test_success_alnum(value, more_chars):
    if more_chars:
        assert v.alnum(*more_chars).validate(value)
        assert v.alnum(*more_chars).claim(value) is None
        assert v.alnum(*more_chars).check(value) is None
    else:
        assert v.alnum().validate(value)
        assert v.alnum().claim(value) is None
        assert v.alnum().check(value) is None


@pytest.mark.parametrize(('more_chars', 'value'), [
    (None, ''),
    (None, 'number 100%'),
    ('%', 'number 100%'),
    (None, '@#$'),
    (None, '_'),
    (None, 1e21),
    (None, None),
    (None, object()),
    (None, []),
    ('%', 'number 100%'),
    (None, "\t"),
    (None, "\n"),
    (None, "\nabc"),
    (None, "\tdef"),
    (None, "\nabc \t"),
    (None, 'alganet alganet'),
])
def test_fail_alnum(value, more_chars):
    if more_chars:
        with pytest.raises(AlnumException, match='must contain only letters \\(a-z\\)'):
            assert v.alnum(*more_chars).check(value)
            assert v.alnum(*more_chars).claim(value)
        assert v.alnum(*more_chars).validate(value) is False
    else:
        with pytest.raises(AlnumException, match='must contain only letters \\(a-z\\)'):
            assert v.alnum().check(value)
            assert v.alnum().claim(value)
        assert v.alnum().validate(value) is False
