# Consonant

- `Consonant(*additional_chars: str)`

Validates if the input contains only consonants.

```python
v.consonant().validate('xkcd')  # true
v.consonant('!@#$').validate('!@xk#$cd')  # true
v.consonant('!@#$', '}{?').validate('{!@xk#$cd}')  # true
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
- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Vowel](Vowel.md)