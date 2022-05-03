# ListType

- `ListType()`

Validates whether the type of an input is list.

```python
v.listType().validate([])  # true
v.listType().validate([1, 2, 3])  # true
v.listType().validate('Am I list?')  # false
```

## Categorization

- Lists
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BoolType](BoolType.md)
- [CallableType](CallableType.md)
- [DictType](DictType.md)
- [Countable](Countable.md)
- [FloatType](FloatType.md)
- [IntType](IntType.md)
- [Iterable](Iterable.md)
- [NoneType](NoneType.md)
- [StringType](StringType.md)
- [Subset](Subset.md)
- [Type](Type.md)
- [Unique](Unique.md)