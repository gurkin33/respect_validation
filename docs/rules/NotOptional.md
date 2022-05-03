# NotOptional

- `NotOptional()`

Validates if the given input is not optional. By _optional_ we consider `None`
or an empty string (`''`).

```python
v.notOptional().validate('')  # false
v.notOptional().validate(None)  # false
```

Other values:

```python
v.notOptional().validate([])  # true
v.notOptional().validate(' ')  # true
v.notOptional().validate(0)  # true
v.notOptional().validate('0')  # true
v.notOptional().validate(0)  # true
v.notOptional().validate('0.0')  # true
v.notOptional().validate(False)  # true
v.notOptional().validate([''])  # true
v.notOptional().validate([' '])  # true
v.notOptional().validate([0])  # true
v.notOptional().validate(['0'])  # true
v.notOptional().validate([False])  # true
v.notOptional().validate([[''], [0]])  # true
v.notOptional().validate(object())  # true
```

## Categorization

- Miscellaneous

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [NoWhitespace](NoWhitespace.md)
- [NotBlank](NotBlank.md)
- [NotEmpty](NotEmpty.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [Optional](Optional.md)