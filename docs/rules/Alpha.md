# Alpha

- `Alpha(*additional_chars: str)`

Validates whether the input contains only alphabetic characters. This is similar
to [Alnum](Alnum.md), but it does not allow numbers.

```python
v.alpha().validate('some name')  # false
v.alpha(' ').validate('some name')  # true
v.alpha().validate('Cedric-Fabian')  # false
v.alpha('-').validate('Cedric-Fabian')  # true
v.alpha('-', '\'').validate('\'s-Gravenhage')  # true
```

You can restrict case using the [Lowercase](Lowercase.md) and
[Uppercase](Uppercase.md) rules.

```python
v.alpha().uppercase().validate('example')  # false
```
_IMPORTANT_ any input value will be converted to string type, except None. You can put any object type except NoneType object. 
You can restrict type by using type rule like [StringType](StringType.md), [IntType](IntType.md) and so on.
```python
v.alpha('[', ']').validate(list())  # True
v.stringType().alpha('[', ']').validate(list())  # false
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
- [Charset](Charset.md)
- [Consonant](Consonant.md)
- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Lowercase](Lowercase.md)
- [NoWhitespace](NoWhitespace.md)
- [Regex](Regex.md)
- [Uppercase](Uppercase.md)
- [Vowel](Vowel.md)