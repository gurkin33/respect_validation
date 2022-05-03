# CreditCard

- `CreditCard(brand: str = 'any')`

Validates a credit card number.

```python
v.creditCard().validate('5376 7473 9720 8720')  # true
v.creditCard().validate('5376-7473-9720-8720')  # true
v.creditCard().validate('5376.7473.9720.8720')  # true
v.creditCard('American Express').validate('340316193809364')  # true
v.creditCard('Diners Club').validate('30351042633884')  # true
v.creditCard('Discover').validate('6011000990139424')  # true
v.creditCard('JCB').validate('3566002020360505')  # true
v.creditCard('MasterCard').validate('5376747397208720')  # true
v.creditCard('Visa').validate('4024007153361885')  # true
```

The current supported brands are:

- American Express (`'American Express'` or `CreditCard.AMERICAN_EXPRESS`)
- Diners Club (`'Diners Club'` or `CreditCard.DINERS_CLUB`)
- Discover (`'Discover'` or `CreditCard.DISCOVER`)
- JCB (`'JCB'` or `CreditCard.JCB`)
- MasterCard (`'MasterCard'` or `CreditCard.MASTERCARD`)
- Visa (`'Visa'` or `CreditCard.VISA`)

It ignores any non-numeric characters, use [Digit](Digit.md),
[NoWhitespace](NoWhitespace.md), or [Regex](Regex.md) when appropriate.

```python
v.digit().creditCard().validate('5376747397208720')  # true
```

## Categorization

- Banking

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Decimal](Decimal.md)
- [Digit](Digit.md)
- [Iban](Iban.md)
- [Luhn](Luhn.md)
- [NoWhitespace](NoWhitespace.md)
- [Regex](Regex.md)