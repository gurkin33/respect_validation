# Type

- `Type(type_name: str)`

Validates the type of input. List of available for validation types:

`list,bool, int,
        str, float, complex,
        list, tuple, range,
        dict, set, frozenset,
        bytes, bytearray, memoryview
        function, NoneType`

```python
def i_am_function():
        pass

v.type('bool').validate(True)  # true
v.type('str').validate('alex')  # true
v.type('function').validate(i_am_function)  # true
v.type('bytes').validate(b'')  # true
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
- [BoolType](BoolType.md)
- [BoolVal](BoolVal.md)
- [CallableType](CallableType.md)
- [Finite](Finite.md)
- [FloatType](FloatType.md)
- [FloatVal](FloatVal.md)
- [Infinite](Infinite.md)
- [Instance](Instance.md)
- [IntType](IntType.md)
- [IntVal](IntVal.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [StringType](StringType.md)
- [StringVal](StringVal.md)