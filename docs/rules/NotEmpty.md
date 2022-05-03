# NotEmpty

- `NotEmpty()`

Validates whether the given input is not empty. This function also takes whitespace
into account, use `noWhitespace()` if no spaces or linebreaks and other
whitespace anywhere in the input is desired.

```python
v.stringType().notEmpty().validate('')  # false
```

Null values are empty:

```python
v.notEmpty().validate(None)  # false
```

Numbers:

```python
v.intVal().notEmpty().validate(0)  # false
```

Empty arrays:

```python
v.listType().notEmpty().validate([])  # false
```

Whitespace:

```python
v.stringType().notEmpty().validate('        ')  # false
v.stringType().notEmpty().validate("\t \n \r")  # false
```

## Categorization

- Miscellaneous

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Each](Each.md)
- [NoWhitespace](NoWhitespace.md)
- [NotBlank](NotBlank.md)
- [NotOptional](NotOptional.md)
- [NoneType](NoneType.md)
- [Number](Number.md)
- [Optional](Optional.md)