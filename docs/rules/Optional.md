# Optional

- `Optional(rule: AbstractRule)`

Validates if the given input is optional or not. By _optional_ we consider `None`
or an empty string (`''`).

```python
v.optional(v.alpha()).validate('')  # true
v.optional(v.digit()).validate(None)  # true
```

## Categorization

- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [NoWhitespace](NoWhitespace.md)
- [NotBlank](NotBlank.md)
- [NotEmpty](NotEmpty.md)
- [NotOptional](NotOptional.md)
- [NoneType](NoneType.md)
- [Nullable](Nullable.md)