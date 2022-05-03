# Equivalent

- `Equivalent(compare_to: Any)`

Validates if the input is equivalent to some value.

```python
v.equivalent(1).validate(True)  # true
v.equivalent('Something').validate('someThing')  # true
v.equivalent([1, 2, 3, 4, 5]).validate([1, 2, 3, 4, 5])  # true
```

This rule is very similar to [Equals](Equals.md) but it does not make case-sensitive
comparisons.

Message template for this validator includes `{compare_to}`.

## Categorization

- Comparisons

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Contains](Contains.md)
- [ContainsAny](ContainsAny.md)
- [Equals](Equals.md)
- [Identical](Identical.md)