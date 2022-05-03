# DateTime

- `DateTime(date_format: Optional[str] = None)`

Validates whether an input is a date/time or not. The `date_format` argument should
be in accordance to datetime [Format Code][] string.

By default, date_format is None but this rule try to convert string to date based on ISO format. 
To convert string to date it uses [fromisoformat][] method.

Input in ISO format:

```python
v.dateTime().validate('2022-01-01')  # true
v.dateTime().validate('2022-01-01 15:11:12')  # true
v.dateTime().validate('2022-01-01T15:11:12')  # true
```

Also accepts datetime instances:

```python
v.dateTime().validate(datetime.fromtimestamp(1657598400))  # true
```

You can pass a format when validating strings:

```python
v.dateTime('%Y-%m-%d').validate('01-01-2009')  # false
v.dateTime('%d-%m-%Y').validate('01-01-2009')  # true
```

Format has no effect when validating datetime instances.

Message template for this validator includes `{sample}` 
which is a sample of an expected date.

```python
try:
    v.dateTime('%Y-%m-%d').check('01-01-2009')
except ValidationException as exception:
    print(exception.get_message())
```

Output:
```text
"01-01-2009" must be a valid date/time in the format 2022-04-26
```

## Categorization

- Date and Time

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Between](Between.md)
- [Date](Date.md)
- [LeapDate](LeapDate.md)
- [LeapYear](LeapYear.md)
- [Time](Time.md)

[Format Code]: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
[fromisoformat]: https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat