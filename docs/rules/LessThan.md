# LessThan

- `LessThan(compare_to: Any)`

Validates whether the input is less than a value.

```python
v.lessThan(10).validate(9)  # true
v.lessThan(10).validate(10)  # false
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