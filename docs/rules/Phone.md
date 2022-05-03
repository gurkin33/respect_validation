# Phone

- `Phone(strict: bool = False)`

Validates whether the input is a valid phone number.

This rule uses library [phonenumbers][]. There are two methods to validate phone number:
- is_possible_number - fast method, didn't do additional checks (strict = False)
- is_valid_number - a little slower, because it does additional checks (strict = True)
You can switch between these two method with `strict` parameter.
  
```python
v.phone().validate('+7 (999) 555 5555')  # true
v.phone().validate('+5(555)555 5555')  # true
v.phone().validate('+33(1)22 22 22 22')  # true
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Email](Email.md)
- [Json](Json.md)
- [Url](Url.md)
- [VideoUrl](VideoUrl.md)

[phonenumbers]: https://pypi.org/project/phonenumbers/