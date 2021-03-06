# Finite

- `Finite()`

Validates if the input is a finite number.

```python
import math

v.finite().validate('10')  # true
v.finite().validate(10)  # true
v.finite().validate(math.inf)  # false
```

## Categorization

- Math
- Numbers

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Factor](Factor.md)
- [Infinite](Infinite.md)
- [IntType](IntType.md)
- [IntVal](IntVal.md)
- [NumericVal](NumericVal.md)
- [Type](Type.md)