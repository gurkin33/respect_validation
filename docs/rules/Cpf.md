# Cpf

- `Cpf()`

Validates a Brazillian CPF number.

```python
v.cpf().validate('11598647644')  # true
```

It ignores any non-digit char:

```python
v.cpf().validate('693.319.118-40')  # true
```

If you need to validate digits only, add `.digit()` to
the chain:

```python
v.digit().cpf().validate('11598647644')  # true
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
- [Cnpj](Cnpj.md)
- [Imei](Imei.md)
- [Pis](Pis.md)