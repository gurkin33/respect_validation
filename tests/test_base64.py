import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions.Base64Exception import Base64Exception

LINES = [
    'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlz',
    'IHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2Yg',
    'dGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGlu',
    'dWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRo',
    'ZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=',
]


@pytest.mark.parametrize('value', [
    'YW55IGNhcm5hbCBwbGVhc3VyZS4=',
    'YW55IGNhcm5hbCBwbGVhc3VyZQ==',
    'YW55IGNhcm5hbCBwbGVhc3Vy',
    'YW55IGNhcm5hbCBwbGVhc3U=',
    'YW55IGNhcm5hbCBwbGVhcw==',
    'cGxlYXN1cmUu',
    'bGVhc3VyZS4=',
    'ZWFzdXJlLg==',
    'YXN1cmUu',
    'c3VyZS4=',
    'WeJcFMQ/8+8QJ/w0hHh+0g==',
    "\n".join(LINES),
    "\r\n".join(LINES)
])
def test_success_base64(value):
    assert v.base64().validate(value)
    assert v.base64().check(value) is None
    assert v.base64().claim(value) is None


@pytest.mark.parametrize('value', [
    '',
    'hello!',
    '=c3VyZS4',
    'YW55IGNhcm5hbCBwbGVhc3VyZ===',
])
def test_fail_base64(value):
    assert v.base64().validate(value) is False

    with pytest.raises(Base64Exception, match="must be Base64-encoded"):
        assert v.base64().check(value)
        assert v.base64().claim(value)
