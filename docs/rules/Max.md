# Max

- `Max(compare_to: Any)`

Validates whether the input is less than or equal to a value.

```python
v.Max(10).validate(9)  # true
v.Max(10).validate(10)  # true
v.Max(10).validate(11)  # false
```

Validation makes comparison easier, check out our supported
[comparable values](../comparable-values.md).

Message template for this validator includes `{compare_to}`.

## Categorization

- Comparisons

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Between](Between.md)
- [GreaterThan](GreaterThan.md)
- [LessThan](LessThan.md)
- [Min](Min.md)