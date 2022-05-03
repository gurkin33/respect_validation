# Instance

- `Instance(instance_name: str)`

Validates if the input is an instance of the given class 
(it doesn't check inheritance).

```python
from datetime import datetime

v.instance('datetime').validate(datetime.today())  # true
v.instance('list').validate([1, 2, 3])  # true
```

Message template for this validator includes `{instance_name}`.

## Categorization

- Objects

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Countable](Countable.md)
- [Iterable](Iterable.md)
- [Type](Type.md)