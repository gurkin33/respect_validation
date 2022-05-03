import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.IsbnException import IsbnException


@pytest.mark.parametrize('value', [
    'ISBN-13: 978-0-596-52068-7',
    '978 0 596 52068 7',
    '9780596520687',
    '0-596-52068-9',
    '0 512 52068 9',
    'ISBN-10 0-596-52068-9',
    'ISBN-10: 0-596-52068-9',
])
def test_success_isbn(value):
    assert v.isbn().validate(value)
    assert v.isbn().check(value) is None
    assert v.isbn().claim(value) is None


@pytest.mark.parametrize('value', [
    [],
    None,
    object(),
    '',
    'ABCDEFGHIKLMNOPQRSTVXYZ',
    'ISBN 11978-0-596-52068-7',
    'ISBN-12: 978-0-596-52068-7',
    '978 10 596 52068 7',
    '119780596520687',
    '0-5961-52068-9',
    '11 5122 52068 9',
    'ISBN-11 0-596-52068-9',
    'ISBN-10- 0-596-52068-9',
    'Defiatly no ISBN',
    'Neither ISBN-13: 978-0-596-52068-7',
])
def test_fail_isbn(value):
    assert v.isbn().validate(value) is False

    with pytest.raises(IsbnException, match=r' must be a ISBN'):
        assert v.isbn().check(value)
        assert v.isbn().claim(value)
