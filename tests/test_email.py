import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.EmailException import EmailException


@pytest.mark.parametrize('value', [
    'test@test.com',
    'mail+mail@gmail.com',
    'mail.email@e.test.com'
])
def test_success_email(value):
    assert v.email().validate(value)
    assert v.email().check(value) is None
    assert v.email().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    'test',
    '@test.com',
    'a@a.a',
    'mail@test@test.com',
    'test.test@',
    'test.@test.com',
    'test@.test.com',
    'test@test..com',
    'test@test.com.',
    '.test@test.com',
    [],
    object(),
    None
])
def test_fail_email(value):
    assert v.email().validate(value) is False

    with pytest.raises(EmailException, match="must be valid email"):
        assert v.email().check(value)
        assert v.email().claim(value)
