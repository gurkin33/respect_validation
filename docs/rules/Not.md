# Not

- `Not(rule: AbstractRule)`

Negates any rule.

```python
v.Not(v.ip()).validate('foo')  # true
```

In the sample above, validator returns true because 'foo' isn't an IP Address.

You can negate complex, grouped or chained validators as well:

```python
v.Not(v.intVal().positive()).validate(-1.5)  # true
```

Each other validation has custom messages for negated rules.

## Categorization

- Conditions
- Nesting

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [NoneOf](NoneOf.md)