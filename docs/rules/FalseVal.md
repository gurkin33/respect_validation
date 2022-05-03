# FalseVal

- `FalseVal()`

Validates if a value is considered as `False`.

```python
v.falseVal().validate(False)  # true
v.falseVal().validate(0)  # true
v.falseVal().validate('0')  # true
v.falseVal().validate('false')  # true
v.falseVal().validate('off')  # true
v.falseVal().validate('no')  # true
v.falseVal().validate('0.5')  # false
v.falseVal().validate('2')  # false
```

## Categorization

- Booleans

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [TrueVal](TrueVal.md)