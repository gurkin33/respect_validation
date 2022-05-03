# Nullable

- `Nullable(rule: AbstractRule)`

Validates the given input with a defined rule when input is not NULL.

```python
v.nullable(v.email()).validate(None)  # true
v.nullable(v.email()).validate('example@example.com')  # true
v.nullable(v.email()).validate('not an email')  # false
```

## Categorization

- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [NoneType](NoneType.md)
- [Optional](Optional.md)