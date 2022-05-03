# Iterable

- `Iterable()`

Validates whether an input has attribute `__iter__` .

```python
v.iterable().validate([])  # true
v.iterable().validate(range(1))  # true
v.iterable().validate(dict())  # true
v.iterable().validate('string')  # true
v.iterable().validate(12)  # false
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
- [Countable](Countable.md)
- [Each](Each.md)
- [Instance](Instance.md)