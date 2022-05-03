# StartsWith

- `StartsWith(start_value: Any)`

Validates whether the input starts with a given value.

This validator is similar to [Contains](Contains.md), but validates only
if the value is at the beginning of the input.

For strings:

```python
v.startsWith('lorem').validate('lorem ipsum')  # true
```

For lists:

```python
v.startsWith('lorem').validate(['lorem', 'ipsum'])  # true
```


Message template for this validator includes `{start_value}`.

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
- [EndsWith](EndsWith.md)
- [Include](Include.md)
- [Regex](Regex.md)