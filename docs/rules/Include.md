# Include

- `Include(haystack: Union[str, List[Any], Tuple[Any]], identical: bool = True)`

Validates if an input contains a specific haystack.

For strings:

```python
v.include('lorem ipsum').validate('ipsum')  # true
```

For lists:

```python
v.include(['lorem', 'ipsum']).validate('lorem')  # true
```

A second parameter may be passed for comparison case-sensitive strings
(default True).

Message template for this validator includes `{haystack}`.

## Categorization

- Arrays
- Comparisons
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Contains](Contains.md)
- [ContainsAny](ContainsAny.md)
- [EndsWith](EndsWith.md)
- [Roman](Roman.md)
- [StartsWith](StartsWith.md)