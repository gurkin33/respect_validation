# NoneOf

- `NoneOf(*rules: Any)`

Validates if NONE of the given validator rules:

```python
v.noneOf(
    v.intVal(),
    v.floatVal()
).validate('foo')  # true
```

In the sample above, 'foo' isn't a integer nor a float, so noneOf returns true.

## Categorization

- Composite
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [AllOf](AllOf.md)
- [AnyOf](AnyOf.md)
- [Not](Not.md)
- [OneOf](OneOf.md)
- [When](When.md)