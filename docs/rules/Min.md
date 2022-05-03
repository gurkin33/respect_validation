# Min

- `Min(compare_to: Any)`

Validates whether the input is greater than or equal to a value.

```python
v.intVal().Min(10).validate(9)  # false
v.intVal().Min(10).validate(10)  # true
v.intVal().Min(10).validate(11)  # true
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
- [Length](Length.md)
- [LessThan](LessThan.md)
- [Max](Max.md)