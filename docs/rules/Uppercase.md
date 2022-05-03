# Uppercase

- `Uppercase()`

Validates whether the characters in the input are uppercase.

```python
v.uppercase().validate('W3C')  # true
```

This rule does not validate if the input a numeric value, so `123` and `%` will
be valid. Please add more validations to the chain if you want to refine your
validation.

```python
v.uppercase().check('42')  # true
v.Not(v.numericVal()).uppercase().validate('42')  # false
v.uppercase().check('#$%!')  # true
v.alnum().uppercase().validate('#$%!')  # false
v.Not(v.numericVal()).alnum().uppercase().validate('W3C')  # true
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Alnum](Alnum.md)
- [Alpha](Alpha.md)
- [Lowercase](Lowercase.md)
- [NumericVal](NumericVal.md)
- [Roman](Roman.md)