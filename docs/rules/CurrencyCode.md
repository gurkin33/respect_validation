# CurrencyCode

- `CurrencyCode(code_set: str = 'alpha-2')`

Validates an [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) currency code like GBP or EUR.

```python
v.currencyCode().validate('GBP')  # true
v.currencyCode('alpha-3').validate('EUR')  # true
v.currencyCode('numeric').validate('840')  # true
```

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

- [CountryCode](CountryCode.md)

[pycountry]: https://pypi.org/project/pycountry/