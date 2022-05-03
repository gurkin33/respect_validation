# LeapDate

- `LeapDate(date_format: str = "%Y-%m-%d")`

Validates if a date is leap.

```python
v.leapDate('%Y-%m-%d').validate('1988-02-29')  # true
```

This validator accepts datetime instances as well. The `date_format`
parameter is mandatory (by default, it is `%Y-%m-%d`).

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
- [LeapYear](LeapYear.md)
- [Time](Time.md)