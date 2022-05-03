# KeySet

- `KeySet(*keys: Key)`

Validates a keys in a defined structure.

```python
test_dict = {'foo': 42}
v.keySet(
    v.key('foo', v.intVal())
).validate(test_dict)  # true
```

Extra keys are not allowed:
```python
test_dict = {'foo': 42, 'bar': 'String'}
v.keySet(
    v.key('foo', v.intVal())
).validate(test_dict)  # false
```

Missing required keys are not allowed:
```python
test_dict = {'foo': 42, 'bar': 'String'}
v.keySet(
    v.key('foo', v.intVal()),
    v.key('bar', v.stringType()),
    v.key('baz', v.boolType())
).validate(test_dict)  # false
```

Missing non-required keys are allowed:
```python
test_dict = {'foo': 42, 'bar': 'String'}
v.keySet(
    v.key('foo', v.intVal()),
    v.key('bar', v.stringType()),
    v.key('baz', v.boolType(), False)
).validate(test_dict)  # true
```

The keys order is not considered in the validation.

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

- [Key](Key.md)
- [KeyValue](KeyValue.md)