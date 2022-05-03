# HexRgbColor

- `HexRgbColor()`

Validates weather the input is a hex RGB color or not.

```python
v.hexRgbColor().validate('#FFFAAA')  # true
v.hexRgbColor().validate('#ff6600')  # true
v.hexRgbColor().validate('123123')  # true
v.hexRgbColor().validate('FCD')  # true
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [CreditCard](CreditCard.md)
- [PostalCode](PostalCode.md)
- [Regex](Regex.md)