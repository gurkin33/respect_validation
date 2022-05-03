# Domain

- `Domain(tld_check: bool = True)`

Validates whether the input is a valid domain name or not.

```python
v.domain().validate('google.com')  # true
```

You can skip *top level domain* (TLD) checks to validate internal
domain names:

```python
v.domain(False).validate('dev.machine.local')  # true
v.domain(True).validate('dev.machine.local')  # false
```

This is a composite validator, it validates several rules
internally:

- If input is an IP address, it fails.
- If input contains whitespace, it fails.
- If input does not contain any dots, it fails.
- If input has less than two parts, it fails.
- Input must end with a top-level-domain to pass (if not skipped).
- Each part must be alphanumeric and not start with an hyphen.
- [PunnyCode][] is accepted for [Internationalizing Domain Names in Applications][IDNA].

Messages for this validator will reflect rules above.

## Categorization

- Internet

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Ip](Ip.md)
- [Json](Json.md)
- [MacAddress](MacAddress.md)
- [Tld](Tld.md)
- [Url](Url.md)

[PunnyCode]: http://en.wikipedia.org/wiki/Punycode "Wikipedia: Punnycode"
[IDNA]: http://en.wikipedia.org/wiki/Internationalized_domain_name#Internationalizing_Domain_Names_in_Applications "Wikipedia: Internationalized domain name"