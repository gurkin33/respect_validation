# PostalCode

- `PostalCode(country_code: str)`

Validates whether the input is a valid postal code or not.

```python
v.postalCode('BR').validate('02179000')  # true
v.postalCode('BR').validate('02179-000')  # true
v.postalCode('US').validate('02179-000')  # false
v.postalCode('US').validate('55372')  # true
v.postalCode('PL').validate('99-300')  # true
```

Message template for this validator includes `{country_code}`.

Extracted from [GeoNames](http://www.geonames.org/).

## Categorization

- Localization
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [CountryCode](CountryCode.md)
- [Iban](Iban.md)