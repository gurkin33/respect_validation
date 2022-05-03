# CountryCode

- `CountryCode(code_set: str = 'alpha-2')`

Validates whether the input is a country code in [ISO 3166-1][] standard.

```python
v.countryCode().validate('BR')  # true
v.countryCode('alpha-2').validate('NL')  # true
v.countryCode('alpha-3').validate('USA')  # true
v.countryCode('numeric').validate('504')  # true
```

This rule supports the three sets of country codes:

- ISO 3166-1 alpha-2 (`'alpha-2'` or `CountryCode.ALPHA2`)
- ISO 3166-1 alpha-3 (`'alpha-3'` or `CountryCode.ALPHA3`)
- ISO 3166-1 numeric (`'numeric'` or `CountryCode.NUMERIC`).

When no `code_set` is defined the rule uses `'alpha-2'` (`CountryCode.ALPHA2`).

This rule uses library [pycountry][].

## Categorization

- ISO codes
- Localization

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [CurrencyCode](CurrencyCode.md)
- [LanguageCode](LanguageCode.md)
- [PostalCode](PostalCode.md)
- [Tld](Tld.md)

[ISO 3166-1]: https://wikipedia.org/wiki/ISO_3166-1
[pycountry]: https://pypi.org/project/pycountry/