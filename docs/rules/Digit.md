# Digit

- `Digit(*additional_chars: str)`

Validates whether the input contains only digits.
Support only string type.

```python
v.digit().validate('020 612 1851')  # false
v.digit(' ').validate('020 612 1851')  # true
v.digit().validate('172.655.537-21')  # false
v.digit('.', '-').validate('172.655.537-21')  # true
```

## Categorization

- Numbers
- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Alnum](Alnum.md)
- [Alpha](Alpha.md)
- [Consonant](Consonant.md)
- [CreditCard](CreditCard.md)
- [Factor](Factor.md)
- [Finite](Finite.md)
- [Infinite](Infinite.md)
- [IntType](IntType.md)
- [IntVal](IntVal.md)
- [NumericVal](NumericVal.md)
- [Regex](Regex.md)
- [Uuid](Uuid.md)
- [Vowel](Vowel.md)