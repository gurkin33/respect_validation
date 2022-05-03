# Attribute

- `Attribute(reference: str, rule: Optional[AbstractRule] = None, mandatory: bool = True)`

Validates an object attribute, even private ones.

```python
class Object(object):
    pass
obj = Object()
obj.foo = 'bar'
v.attribute('foo').validate(obj)  # true
```

You can also validate the attribute itself:

```python
v.attribute('foo', v.equals('bar')).validate(obj)  # true
```

Third parameter makes the attribute presence optional (default True):

```python
v.attribute('lorem', v.stringType(), False).validate(obj)  # true
v.attribute('alexey', v.stringType(), mandatory=False).validate(obj)  # true
v.attribute('alexey', v.stringType(), mandatory=True).validate(obj)  # false
```

The name of this validator is automatically set to the attribute name.

## Categorization

- Nesting
- Objects
- Structures

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Key](Key.md)