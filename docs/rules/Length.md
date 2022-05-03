# Length

- `Length(min_value: Optional[int] = None, max_value: Optional[int] = None, inclusive: bool = True)`

Validates the length of the given input.

Most simple example:

```python
v.stringType().length(1, 5).validate('abc')  # true
```

You can also validate only minimum length:

```python
v.stringType().length(5, None).validate('abcdef')  # true
v.stringType().length(5).validate('abcdef')  # true
v.stringType().length(min_value=5).validate('abcdef')  # true
```

Only maximum length:

```python
v.stringType().length(None, 5).validate('abc')  # true
v.stringType().length(max_value=5).validate('abc')  # true
```

The type as the first validator in a chain is a good practice,
since length accepts many types:

```python
v.listType().length(1, 5).validate(['foo', 'bar'])  # true
```

A third parameter may be passed to validate the passed values inclusive:

```python
v.stringType().length(1, 5, True).validate('a')  # true
v.stringType().length(1, 5, False).validate('a')  # false
```

Message template for this validator includes `{min_value}` and `{max_value}`.

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Between](Between.md)
- [Min](Min.md)