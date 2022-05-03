# NotBlank

- `NotBlank()`

Validates if the given input is not a blank value (`None`, zeros, empty strings
or empty arrays).

```python
v.notBlank().validate(None)  # false
v.notBlank().validate('')  # false
v.notBlank().validate([])  # false
v.notBlank().validate(' ')  # false
v.notBlank().validate(0)  # false
v.notBlank().validate('0')  # false
v.notBlank().validate(0)  # false
v.notBlank().validate(False)  # false
v.notBlank().validate([''])  # false
v.notBlank().validate([' '])  # false
v.notBlank().validate([0])  # false
v.notBlank().validate(['0'])  # false
v.notBlank().validate([False])  # false

v.notBlank().validate('0.0')  # true
v.notBlank().validate([[''], [0]])  # true
```

It's similar to [NotEmpty](NotEmpty.md) but it's way more strict.

## Categorization

- Miscellaneous

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [NoWhitespace](NoWhitespace.md)
- [NotEmpty](NotEmpty.md)
- [NotOptional](NotOptional.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [Optional](Optional.md)