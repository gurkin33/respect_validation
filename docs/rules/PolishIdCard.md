# PolishIdCard

- `PolishIdCard()`

Validates whether the input is a Polish identity card (Dowód Osobisty).

```python
v.polishIdCard().validate('AYW036733')  # true
v.polishIdCard().validate('APH505567')  # true
v.polishIdCard().validate('APH 505567')  # false
v.polishIdCard().validate('AYW036731')  # false
```

## Categorization

- Identifications

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Nip](Nip.md)
- [Pesel](Pesel.md)