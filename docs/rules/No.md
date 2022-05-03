# No

- `No()`

Validates if value is considered as "No".

```python
v.no().validate('N')  # true
v.no().validate('Nay')  # true
v.no().validate('Nix')  # true
v.no().validate('No')  # true
v.no().validate('Nope')  # true
v.no().validate('Not')  # true
```

This rule is case-insensitive.

## Categorization

- Booleans

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BoolType](BoolType.md)
- [BoolVal](BoolVal.md)
- [Yes](Yes.md)