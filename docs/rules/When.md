# When

- `When(if_rule: AbstractRule, then_rule: AbstractRule, else_rule: Optional[AbstractRule] = None)`

A ternary validator that accepts three parameters.

When the `if_rule` validates, returns validation for `then_rule`.
When the `if_rule` doesn't validate, returns validation for `else_rule`, if defined.

```python
v.when(v.intVal(), v.positive(), v.notEmpty()).validate(1)  # true
v.when(v.intVal(), v.positive(), v.notEmpty()).validate('not empty')  # true
v.when(v.intVal(), v.positive(), v.notEmpty()).validate(-1)  # false
v.when(v.intVal(), v.positive(), v.notEmpty()).validate('')  # false
```

In the sample above, if `input_value` is an integer, then it must be positive.
If `input_value` is not an integer, then it must not be empty.
When `else_rule` is not defined use [AlwaysInvalid](AlwaysInvalid.md)

## Categorization

- Conditions
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [AllOf](AllOf.md)
- [AlwaysInvalid](AlwaysInvalid.md)
- [AnyOf](AnyOf.md)
- [NoneOf](NoneOf.md)
- [OneOf](OneOf.md)