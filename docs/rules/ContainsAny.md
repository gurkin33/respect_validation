# ContainsAny

- `ContainsAny(needles: List[Any], identical: bool = True)`

Validates if the input contains at least one of defined values

For strings (comparing is case-insensitive):

```python
v.containsAny(['lorem', 'dolor'], identical=False).validate('loReM ipsum')  # true
```

For lists (comparing is case-sensitive to respect "contains" behavior):

```python
v.containsAny(['lorem', 'dolor']).validate(['ipsum', 'lorem'])  # true
v.containsAny(['lorem', 'dolor']).validate(['ipsum', 'lOrEm'])  # false
```

A second parameter may be passed for comparison of strings as case-insensitive (default True).

Message template for this validator includes `{needles}`.

## Categorization

- Arrays
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [AnyOf](AnyOf.md)
- [Contains](Contains.md)
- [Equivalent](Equivalent.md)
- [Include](Include.md)