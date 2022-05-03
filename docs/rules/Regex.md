# Regex

- `Regex(regex: Union[str, Pattern[str]])`

Validates whether the input matches a defined regular expression. You can set string or `re.Pattern` 
(output of `re.compile()`) for regex pattern.

```python
v.regex('[a-z]').validate('a')  # true
v.regex(re.compile('[a-z]')).validate('a')  # true
```

Message template for this validator includes `{regex}`.

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
- [Contains](Contains.md)
- [CreditCard](CreditCard.md)
- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [EndsWith](EndsWith.md)
- [Roman](Roman.md)
- [StartsWith](StartsWith.md)
- [Version](Version.md)