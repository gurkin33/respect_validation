# Key

- `Key(reference: str, rule=None, mandatory: bool = True)`

Validates an array key.

```python
test_dict = {
    'foo': 'bar'
}
v.key('foo').validate(test_dict)  # true
```

You can also validate the key value itself:

```python
v.key('foo', v.equals('bar')).validate(test_dict)  # true
```

Third parameter makes the key presence optional:

```python
v.key('lorem', v.stringType()).validate(test_dict)  # false
v.key('lorem', v.stringType(), False).validate(test_dict)  # true
```

The name of this validator is automatically set to the key name.

## Categorization

- Arrays
- Nesting
- Structures

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Attribute](Attribute.md)
- [Each](Each.md)
- [KeySet](KeySet.md)
- [KeyValue](KeyValue.md)