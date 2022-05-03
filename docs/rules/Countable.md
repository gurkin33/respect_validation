# Countable

- `Countable()`

Validates if the input is countable, 
in other words, if input has `__len__` attribute.

```python
v.countable().validate([])  # true
v.countable().validate(range(10))  # true
v.countable().validate(100)  # false
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
- [Instance](Instance.md)
- [Iterable](Iterable.md)