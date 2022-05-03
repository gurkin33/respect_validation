# BaseNum

- `BaseNum(base: int, chars: Optional[str] = None)`

Validate numbers in any base, even with non-regular bases.

```python
v.baseNum(2).validate('011010001')  # true
v.baseNum(3).validate('0120122001')  # true
v.baseNum(8).validate('01234567520')  # true
v.baseNum(16).validate('012a34f5675c20d')  # true
v.baseNum(2).validate('0120122001')  # false
```

## Categorization

- Numbers

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Base64](Base64.md)
- [Uuid](Uuid.md)