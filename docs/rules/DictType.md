# DictType

- `DictType()`

Validates whether an input is type of dict.

```python
v.dictType().validate(dict())  # true
v.dictType().validate({})  # true
v.dictType().validate({'hello': 'world'})  # true
v.dictType().validate('Am I dict?')  # false
```

## Categorization

- Lists
- Arrays
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BoolType](BoolType.md)
- [CallableType](CallableType.md)
- [Countable](Countable.md)
- [FloatType](FloatType.md)
- [IntType](IntType.md)
- [Iterable](Iterable.md)
- [NoneType](NoneType.md)
- [StringType](StringType.md)
- [Subset](Subset.md)
- [Type](Type.md)
- [Unique](Unique.md)