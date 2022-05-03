# LanguageCode

- `LanguageCode(code_set: str = 'alpha-2')`

Validates whether the input is language code based on ISO 639.

```python
v.languageCode().validate('pt') # true
v.languageCode().validate('en') # true
v.languageCode().validate('it') # true
v.languageCode('alpha-3').validate('ita') # true
v.languageCode('alpha-3').validate('eng') # true
```

You can choose `code_set` between `alpha-2` and `alpha-3`; `alpha-2` is set by default.

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