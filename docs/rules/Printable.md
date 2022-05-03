# Printable

- `Printable(*additional_chars: str)`

This rule checks if all characters in the input are printable.

Characters that occupy printing space on the screen are known as printable characters. For example:
- letters and symbols
- digits
- punctuation
- whitespace

```python
v.printable().validate('LMKA0$% _123')  # true
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Control](Control.md)
- [Punct](Punct.md)