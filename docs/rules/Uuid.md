# Uuid

- `Uuid(version: Union[Optional[int], Optional[str]] = None))`

Validates whether the input is a valid UUID. It also supports validation of
specific versions 1, 3, 4 and 5.

```python
v.uuid().validate('Hello World!')  # false
v.uuid().validate('eb3115e5-bd16-4939-ab12-2b95745a30f3')  # true
v.uuid(1).validate('eb3115e5-bd16-4939-ab12-2b95745a30f3')  # false
v.uuid(4).validate('eb3115e5-bd16-4939-ab12-2b95745a30f3')  # true
```

## Categorization

- Strings

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [BaseNum](BaseNum.md)
- [Decimal](Decimal.md)
- [Digit](Digit.md)