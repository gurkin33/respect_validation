# CallableType

- `CallableType()`

Validates if the specified object is callable.

```python
v.callableType().validate(object)  # true
v.callableType().validate(str)  # true
v.callableType().validate('Am I True?'.lower)  # true
```

## Categorization

- Callables
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [ListType](ListType.md)
- [BoolType](BoolType.md)
- [BoolVal](BoolVal.md)
- [Callback](Callback.md)
- [FloatType](FloatType.md)
- [IntType](IntType.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [StringType](StringType.md)
- [StringVal](StringVal.md)
- [Type](Type.md)