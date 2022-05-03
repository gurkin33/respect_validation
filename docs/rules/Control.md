# Control

- `Control(*additional_chars: str)`

Validates if all characters in the provided string, are control
characters.

```python
v.control().validate("\n\r\t")  # true
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
- [Printable](Printable.md)
- [Punct](Punct.md)
- [Space](Space.md)