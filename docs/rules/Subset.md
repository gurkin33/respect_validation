# Subset

- `Subset(superset: Union[List[Any], Tuple[Any], Set[Any], range])`

Validates whether the input is a subset of a given value.

```python
v.subset([1, 2, 3]).validate([1, 2])  # true
v.subset([1, 2]).validate([1, 2, 3])  # false
```

## Categorization

- Arrays

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [ListType](ListType.md)