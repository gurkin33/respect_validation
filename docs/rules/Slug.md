# Slug

- `Slug()`

Validates whether the input is a valid slug.

```python
v.slug().validate('my-wordpress-title')  # true
v.slug().validate('my-wordpress--title')  # false
v.slug().validate('my-wordpress-title-')  # false
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Url](Url.md)
- [VideoUrl](VideoUrl.md)