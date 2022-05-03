# Ip

- `Ip(range: str = '*', private: bool = False)`

Validates whether the input is a valid IP address.

This validator uses the library [ipaddress][].

```python
v.ip().validate('127.0.0.1')  # true
v.ip('192.168.100.100-192.168.200.200').validate('192.168.150.150')  # true
v.ip('220.78.168.0/21').validate('220.78.173.2')  # true
v.ip('220.78.168.0/21').validate('220.78.176.2')  # false
```

If you want to validate private ip addresses, please add `private=True`:

```python
v.ip(private=True).validate('10.1.1.1')  # true
v.ip('*', True).validate('172.16.2.2')  # true
v.ip('*', True).validate('2.2.2.2')  # false
```

## Categorization

- Internet

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Domain](Domain.md)
- [MacAddress](MacAddress.md)
- [Tld](Tld.md)

[ipaddress]: https://docs.python.org/3/library/ipaddress.html