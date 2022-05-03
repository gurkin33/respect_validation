# Charset

- `Charset(*args: str)`

Validates if a string is in a specific charset.

```python
v.charset('ASCII').validate('açúcar')  # false
v.charset('ASCII').validate('sugar')  # true
v.charset('EUC-JP', 'ISO-8859-1').validate('açaí'.encode('ISO-8859-1'))  # true
```

The list of charsets has a logic OR, not AND.

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Alnum](Alnum.md)
- [Alpha](Alpha.md)