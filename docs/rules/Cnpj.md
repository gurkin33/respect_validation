# Cnpj

- `Cnpj()`

Validates if the input is a Brazilian National Registry of Legal Entities (CNPJ) number.
Ignores non-digit chars, so use `.digit()` if needed.

```python
v.cnpj().validate('38175021000110')  # true
v.cnpj().validate('32.063.364/0001-07')  # true
```

## Categorization

- Identifications

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Bsn](Bsn.md)
- [Cnh](Cnh.md)
- [Cpf](Cpf.md)
- [Imei](Imei.md)
- [Pis](Pis.md)