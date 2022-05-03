# Isbn

- `Isbn()`

Validates whether the input is a valid [ISBN][] or not.

```python
v.isbn().validate('ISBN-13: 978-0-596-52068-7')  # true
v.isbn().validate('978 0 596 52068 7')  # true
v.isbn().validate('ISBN-12: 978-0-596-52068-7')  # false
v.isbn().validate('978 10 596 52068 7')  # false
```

## Categorization

- Identifications

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Imei](Imei.md)
- [Luhn](Luhn.md)

[ISBN]: https://www.isbn-international.org/content/what-isbn "International Standard Book Number"