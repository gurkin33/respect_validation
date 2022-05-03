# Time

- `Time(date_format: str = '%H:%M:%S')`

Validates if input is a date. The `date_format` argument should be in accordance to
datetime [Format Code][] string.

When a `date_format` is not given its default value is `%H:%M:%S`.

If input is instance of datetime, then it is treated as valid.

```python
v.time().validate('00:00:00')  # true
v.time().validate('23:20:59')  # true
v.time('%H:%M').validate('23:59')  # true
v.time('%H%M%S').validate(232059)  # false
v.time().validate('24:00:00')  # false
v.time().validate(datetime.now())  # true
```

## Categorization

- Date and Time

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Date](Date.md)
- [DateTime](DateTime.md)
- [LeapDate](LeapDate.md)
- [LeapYear](LeapYear.md)

[Format Code]: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes