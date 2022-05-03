# BytesType

- `BytesType()`

Validates whether the type of the input is bytes.

```python
v.bytesType().validate('alexey'.encode())  # true
v.bytesType().validate(b'bytes')  # true
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