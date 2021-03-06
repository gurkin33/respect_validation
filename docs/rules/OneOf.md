# OneOf

- `OneOf(*rules: Any)`

Will validate if exactly one inner validator passes.

```python
v.oneOf(v.digit(), v.alpha()).validate('AB')  # true
v.oneOf(v.digit(), v.alpha()).validate('12')  # true
v.oneOf(v.digit(), v.alpha()).validate('AB12')  # false
v.oneOf(v.digit(), v.alpha()).validate('*')  # false
```

The chains above validate if the input is either a digit or an alphabetic
character, one or the other, but not neither nor both.

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
- [NoneOf](NoneOf.md)
- [When](When.md)