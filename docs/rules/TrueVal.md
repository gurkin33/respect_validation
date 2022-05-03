# TrueVal

- `TrueVal()`

Validates if a value is considered as `True`.

```python
v.trueVal().validate(True)  # true
v.trueVal().validate(1)  # true
v.trueVal().validate('1')  # true
v.trueVal().validate('true')  # true
v.trueVal().validate('on')  # true
v.trueVal().validate('yes')  # true
v.trueVal().validate('0.5')  # false
v.trueVal().validate('2')  # false
```

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
- [FalseVal](FalseVal.md)