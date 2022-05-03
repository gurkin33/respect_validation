# Url

- `Url(public: bool = False)`

Validates whether the input is a URL.
This rule uses validation from [kvesteri/validators][].

```python
v.url().validate('http://example.com')  # true
v.url().validate('http://example.com123')  # false
v.url().validate('https://www.youtube.com/watch?v=6FOUqQt3Kg0')  # true
v.url().validate('ftp://ftp.is.co.za.example.org/rfc/rfc1808.txt')  # true
v.url().validate('http://10.0.0.1')  # true
v.url(public=True).validate('http://10.0.0.1')  # false
```

Set `public` as True to only allow a public IP address.

## Categorization

- Internet

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Domain](Domain.md)
- [Email](Email.md)
- [Phone](Phone.md)
- [Slug](Slug.md)
- [VideoUrl](VideoUrl.md)

[kvesteri/validators]: https://github.com/kvesteri/validators/blob/master/validators/url.py