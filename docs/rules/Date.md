# Date

- `Date(date_format: str = '%Y-%m-%d')`

Validates if input is a date. The `date_format` argument should be in accordance to
datetime [Format Code][] string.

When a `date_format` is not given its default value is `%Y-%m-%d`.

If input is instance of datetime, then it is treated as valid.

```python
v.date().validate('2017-12-31')  # true
v.date().validate('2020-02-29')  # true
v.date().validate('2019-02-29')  # false
v.date('%m/%d/%y').validate('12/31/17')  # true
v.date('%b %d, %Y').validate('May 1, 2022')  # true
v.date('%Y%d%m').validate('20173112')  # true
```

## Categorization

- Date and Time

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [DateTime](DateTime.md)
- [LeapDate](LeapDate.md)
- [LeapYear](LeapYear.md)
- [Time](Time.md)

[Format Code]: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes