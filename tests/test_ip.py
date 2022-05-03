import pytest
import respect_validation.Validator as v
from respect_validation.Exceptions import ComponentException
from respect_validation.Exceptions.IpException import IpException


@pytest.mark.parametrize('params, value', [
    [('127.0.0.0-127.0.0.255',), '127.0.0.1'],
    [('192.168.0.0-192.168.255.255',), '192.168.2.6'],
    [('192.0.0.0-192.255.255.255',), '192.168.2.6'],
    [('0.0.0.0-255.255.255.255',), '192.168.2.6'],
    [('220.78.168.0/21',), '220.78.173.2'],
    [('220.78.168.0/255.255.248.0',), '220.78.173.2'],
    [tuple(), '192.168.255.156'],
    [('*', True,), '192.168.0.1'],
    [('*', True,), '2001:0db8:85a3:08d3:1319:8a2e:0370:7334'],
])
def test_success_ip(params, value):
    assert v.ip(*params).validate(value)
    assert v.ip(*params).check(value) is None
    assert v.ip(*params).claim(value) is None


@pytest.mark.parametrize('params,value', [
    [tuple(), ''],
    [tuple(), None],
    [tuple(), 'j'],
    [tuple(), ' '],
    [tuple(), 'Foo'],
    [('127.0.1.0-127.0.1.255',), '127.0.0.1'],
    [('192.163.0.0-192.163.255.255',), '192.168.2.6'],
    [('193.168.0.0-193.255.255.255',), '192.10.2.6'],
    [('220.78.168.0/21',), '220.78.176.2'],
    [('220.78.168.0/255.255.248.0',), '220.78.176.3'],
])
def test_fail_ip(params, value):
    assert v.ip(*params).validate(value) is False

    with pytest.raises(IpException, match=r' must be an IP address'):
        assert v.ip(*params).check(value)
        assert v.ip(*params).claim(value)


@pytest.mark.parametrize('params,value', [
    [('127.*',), '192.0.1.0'],
    [('127.*',), '127.0.0.1'],
    [('127.0.*',), '127.0.0.1'],
    [('127.0.0.*',), '127.0.0.1'],
    [('192.168.*.6',), '192.168.2.6'],
    [('192.*.2.6',), '192.168.2.6'],
    [('*.168.2.6',), '10.168.2.6'],
    [('192.168.*.*',), '192.168.2.6'],
    [('192.*.*.*',), '192.168.2.6'],
    [('*.*.*.*',), '192.168.255.156'],
    [('127.0.1.*',), '127.0.0.1'],
    [('192.163.*.*',), '192.168.2.6'],
    [('193.*.*.*',), '192.10.2.6'],
    [('220.78.168/21',), '220.78.173.2'],
    [('220.78.168/21',), '220.78.176.1'],
])
def test_fail_ip2(params, value):

    with pytest.raises(ComponentException, match=r'Invalid network range'):
        assert v.ip(*params).validate(value)
        assert v.ip(*params).check(value)
        assert v.ip(*params).claim(value)
