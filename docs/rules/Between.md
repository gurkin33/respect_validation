# Between

- `Between(min_val: Any, max_val: Any)`

Validates whether the input is between two other values.

```python
v.intVal().between(10, 20).validate(10)  # true
v.intVal().between(10, 20).validate(15)  # true
v.intVal().between(10, 20).validate(20)  # true
```

Validation makes comparison easier, check out our supported
[comparable values](../comparable-values.md).

```python
yesterday = datetime.today() - timedelta(days=1)
tomorrow = datetime.today() + timedelta(days=1)
now = datetime.today()

v.dateTime()\
    .between(yesterday, tomorrow)\
    .validate(now)  # true

v.dateTime().between('2022-04-01', '2022-04-15').validate('2022-04-07 10:12:11')  # true
```

Message template for this validator includes `{{min_value}}` and `{{max_value}}`.

## Categorization

- Comparisons

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [DateTime](DateTime.md)
- [GreaterThan](GreaterThan.md)
- [Length](Length.md)
- [LessThan](LessThan.md)
- [Max](Max.md)
- [Min](Min.md)