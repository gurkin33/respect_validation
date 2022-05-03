# GreaterThan

- `GreaterThan(compare_to: Any)`

Validates whether the input is greater than a value.

```python
v.greaterThan(10).validate(11)  # true
v.greaterThan(10).validate(9)  # false
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
- [Max](Max.md)
- [Min](Min.md)