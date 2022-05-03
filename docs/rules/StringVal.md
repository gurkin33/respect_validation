# StringVal

- `StringVal()`

Validates whether the input can be used as a string. It checks if input has attribute `__str__`.

```python
v.stringVal().validate('6')  # true
v.stringVal().validate('String')  # true
v.stringVal().validate(1.0)  # true
v.stringVal().validate(42)  # true
v.stringVal().validate(False)  # true
v.stringVal().validate(True)  # true
```
<sub><sup>Does Python have some object without `__str__` attribute?</sup></sub>

## Categorization

- Strings
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Alnum](Alnum.md)
- [BoolType](BoolType.md)
- [CallableType](CallableType.md)
- [FloatType](FloatType.md)
- [IntType](IntType.md)
- [NoneType](NoneType.md)
- [StringType](StringType.md)
- [Type](Type.md)