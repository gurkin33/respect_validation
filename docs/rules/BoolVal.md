# BoolVal

- `BoolVal()`

Boolean values for this rule are `[0, 1, True, False, '0', '1', 'yes', 'no', 'on', 'off', 'true', 'false']` (all string values compare as lowercase).
  
Validates if the input results in a boolean value:

```python
v.boolVal().validate('on')  # true
v.boolVal().validate('off')  # true
v.boolVal().validate('yes')  # true
v.boolVal().validate('no')  # true
v.boolVal().validate(1)  # true
v.boolVal().validate(0)  # true
```

## Categorization

- Booleans
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BoolType](BoolType.md)
- [CallableType](CallableType.md)
- [FloatType](FloatType.md)
- [FloatVal](FloatVal.md)
- [IntType](IntType.md)
- [No](No.md)
- [NoneType](NoneType.md)
- [StringType](StringType.md)
- [TrueVal](TrueVal.md)
- [Type](Type.md)
- [Yes](Yes.md)