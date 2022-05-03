# Email

- `Email(whitelist: Optional[List[str]] = None)`

Validates an email address.

```python
v.email().validate('amochalini@gmail.com')  # true
```

This rule uses validation from [kvesteri/validators][] and also at the end 
I added addition regex from [emailregex.com][] because the first validator can pass emails 
which ends with _-_ (dash).

You can add `whitelist` - domain names which will be treated as whitelist, by default is has one value - 'localhost'.

## Categorization

- Internet

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Domain](Domain.md)
- [Json](Json.md)
- [Phone](Phone.md)
- [Url](Url.md)
- [VideoUrl](VideoUrl.md)

[emailregex.com]: https://emailregex.com/
[kvesteri/validators]: https://github.com/kvesteri/validators/blob/master/validators/email.py