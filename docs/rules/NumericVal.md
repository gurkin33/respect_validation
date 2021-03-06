# NumericVal

- `NumericVal()`

Validates whether the input is numeric.

```python
v.numericVal().validate(-12)  # true
v.numericVal().validate('135.0')  # true
```

This rule doesn't validate if the input is a valid number, for that
purpose use the [Number](Number.md) rule.

## Categorization

- Numbers
- Types

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Factor](Factor.md)
- [Finite](Finite.md)
- [FloatType](FloatType.md)
- [Infinite](Infinite.md)
- [IntType](IntType.md)
- [IntVal](IntVal.md)
- [Number](Number.md)
- [Uppercase](Uppercase.md)