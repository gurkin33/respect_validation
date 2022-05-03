# EndsWith

- `EndsWith(end_value: Union[str, List[Any], Tuple[Any]])`

This validator is similar to `Contains()`, but validates
only if the value is at the end of the input.

For strings:

```python
v.endsWith('ipsum').validate('lorem ipsum')  # true
```

For arrays:

```python
v.endsWith('ipsum').validate(['lorem', 'ipsum'])  # true
```

Message template for this validator includes `{end_value}`.

## Categorization

- Arrays
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Contains](Contains.md)
- [Include](Include.md)
- [Regex](Regex.md)
- [StartsWith](StartsWith.md)