# AllOf

- `AllOf(*rules: Any)`

Will validate if all inner validators validates.

```python
v.allOf(v.intVal(), v.positive()).validate(15)  # true
```

## Categorization

- Composite
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [AnyOf](AnyOf.md)
- [NoneOf](NoneOf.md)
- [OneOf](OneOf.md)
- [When](When.md)