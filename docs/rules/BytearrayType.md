# BytearrayType

- `BytearrayType()`

Validates whether the type of the input is bytearray.

```python
v.bytearrayType().validate(bytearray(b'hello world!'))  # true
v.bytearrayType().validate(bytearray([94, 91, 101, 125]))  # true
```

## Categorization

- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [ListType](ListType.md)
- [CallableType](CallableType.md)
- [FloatType](FloatType.md)
- [FloatVal](FloatVal.md)
- [IntType](IntType.md)
- [No](No.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [StringType](StringType.md)
- [StringVal](StringVal.md)
- [TrueVal](TrueVal.md)
- [Type](Type.md)
- [Yes](Yes.md)