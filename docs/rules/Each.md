# Each

- `Each(rule: AbstractRule)`

Validates whether each value in the input is valid according to another rule.

```python
release_dates = {
    'validation': '2010-01-01',
    'template'  : '2011-01-01',
    'relational': '2011-02-05',
}
v.each(v.dateTime()).validate(release_dates.values())  # true
```

You can also validate array keys combining this rule with [Call](Call.md):

```python
v.call('values', v.each(v.stringType())).validate(release_dates)  # true
```

This rule will not validate values that are not iterable (don't have attribute `__iter__`), to have a more detailed
error message, add [Iterable](Iterable.md) to your chain, for example.

If the input is empty list then this rule will consider the value as valid, please use
[NotEmpty](NotEmpty.md) if required:

```python
v.each(v.dateTime()).validate([])  # true
v.notEmpty().each(v.dateTime()).validate([])  # false
```

## Categorization

- Arrays
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Call](Call.md)
- [Iterable](Iterable.md)
- [Key](Key.md)
- [NotEmpty](NotEmpty.md)
- [Unique](Unique.md)