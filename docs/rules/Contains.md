# Contains

- `Contains(contains_value, identical: bool = True)`

Validates if the input contains some value.

For strings:

```python
v.contains('ipsum').validate('lorem ipsum')  # true
```

For lists:

```python
v.contains('ipsum').validate(['ipsum', 'lorem'])  # true
```

A second parameter may be passed for comparison of strings as case-insensitive (default True).

Message template for this validator includes `{contains_value}`.

## Categorization

- Arrays
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [ContainsAny](ContainsAny.md)
- [EndsWith](EndsWith.md)
- [Equals](Equals.md)
- [Equivalent](Equivalent.md)
- [Identical](Identical.md)
- [Include](Include.md)
- [Regex](Regex.md)
- [StartsWith](StartsWith.md)
- [Unique](Unique.md)