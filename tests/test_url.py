import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.UrlException import UrlException


@pytest.mark.parametrize('value', [
    'http://www.ietf.org/rfc/rfc2396.txt',
    'ftp://ftp.is.co.za.example.org/rfc/rfc1808.txt',
    'http://www.math.uio.no.example.net/faq/compression-faq/part1.html',
    'https://www.youtube.com/watch?v=6FOUqQt3Kg0',
])
def test_success_url(value):
    assert v.url().validate(value)
    assert v.url().check(value) is None
    assert v.url().claim(value) is None


@pytest.mark.parametrize('value', [
    'example.com',
    'http:/example.com/',
    'tel:+1-816-555-1212',
    'urn:oasis:names:specification:docbook:dtd:xml:4.1.2',
    'mailto:John.Doe@example.com',
    'mailto:mduerst@ifi.unizh.example.gov',
    'telnet://192.0.2.16:80/',
    'telnet://melvyl.ucop.example.edu/',
    'news:comp.infosystems.www.servers.unix',
    'news:comp.infosystems.www.servers.unix',
    'ldap://[2001:db8::7]/c=GB?objectClass?one',
    'gopher://spinaltap.micro.umn.example.edu/00/Weather/California/Los%20Angeles',
])
def test_fail_url(value):
    assert v.url().validate(value) is False

    with pytest.raises(UrlException, match=r' must be a URL'):
        assert v.url().check(value)
        assert v.url().claim(value)
