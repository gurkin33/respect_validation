# Alnum

- `Alnum(*additional_chars: str)`

Validates whether the input is alphanumeric or not.

Alphanumeric is a combination of alphabetic (a-z and A-Z) and numeric (0-9)
characters.

```python
v.alnum().validate('foo 123')  # false
v.alnum(' ').validate('foo 123')  # true
v.alnum().validate('100%')  # false
v.alnum('%').validate('100%')  # true
v.alnum('%', ',').validate('10,5%') #  true
```

You can restrict case using the [Lowercase](Lowercase.md) and
[Uppercase](Uppercase.md) rules.

```python
v.alnum().uppercase().validate('example')  # false
```

_IMPORTANT_ any input value will be converted to string type, except None. You can put any object type except NoneType object. 
You can restrict type by using type rule like [StringType](StringType.md), [IntType](IntType.md) and so on.
```python
v.alnum().validate(123456)  # True
v.stringType().alnum().validate(123456)  # false
```

Message template for this validator includes `{additional_chars}` as the string
of extra chars passed as the parameter.

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Alpha](Alpha.md)
- [Charset](Charset.md)
- [Consonant](Consonant.md)
- [Control](Control.md)
- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Lowercase](Lowercase.md)
- [NoWhitespace](NoWhitespace.md)
- [Regex](Regex.md)
- [StringType](StringType.md)
- [StringVal](StringVal.md)
- [Uppercase](Uppercase.md)
- [Vowel](Vowel.md)