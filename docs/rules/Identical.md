# Identical

- `Identical(compare_to: Any)`

Validates if the input is identical to some value - it should be equal and 
has the same type.

```python
v.identical(42).validate(42)  # true
v.identical(42).validate('42')  # false
```

Message template for this validator includes `{compare_to}`.

## Categorization

- Comparisons

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Contains](Contains.md)
- [Equals](Equals.md)
- [Equivalent](Equivalent.md)