# Yes

- `Yes()`

Validates if the input considered as "Yes".

```python
v.yes().validate('Y')  # true
v.yes().validate('Yea')  # true
v.yes().validate('Yeah')  # true
v.yes().validate('Yep')  # true
v.yes().validate('Yes')  # true
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
- [No](No.md)