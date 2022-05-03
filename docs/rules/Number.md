# Number

- `Number()`

Validates if the input is a number.

```python
v.number().validate(42)  # true
v.number().validate(math.nan)  # false
```

> "In computing, NaN, standing for not a number, is a numeric data type value
> representing an undefined or unrepresentable value, especially in
> floating-point calculations." [Wikipedia](https://en.wikipedia.org/wiki/NaN)
## Categorization

- Numbers

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BoolType](BoolType.md)
- [CallableType](CallableType.md)
- [FloatType](FloatType.md)
- [IntType](IntType.md)
- [NotBlank](NotBlank.md)
- [NotEmpty](NotEmpty.md)
- [NotOptional](NotOptional.md)
- [NoneType](NoneType.md)
- [NumericVal](NumericVal.md)
- [StringType](StringType.md)
- [Type](Type.md)