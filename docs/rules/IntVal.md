# IntVal

- `IntVal()`

Validates if the input is an integer, allowing leading zeros and other number bases.

```python
v.intVal().validate('10')  # true
v.intVal().validate('089')  # true
v.intVal().validate(10)  # true
v.intVal().validate(0b101010)  # true
v.intVal().validate(0x2a)  # true
```

This rule will consider as valid any input that has type int or is string 
which return True for method `isdigit`. `True` and `False` have int type 
then validation will be passed.

```python
v.intVal().validate(True)  # True
v.intVal().validate('89a')  # false
```

## Categorization

- Numbers
- Types

## Changelog

Version  | Description
---------|-------------
  1.0.0  | Created

***
See also:

- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Finite](Finite.md)
- [FloatType](FloatType.md)
- [FloatVal](FloatVal.md)
- [Infinite](Infinite.md)
- [IntType](IntType.md)
- [NumericVal](NumericVal.md)
- [Type](Type.md)