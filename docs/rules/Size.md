# Size

- `Size(min_size: Optional[str] = None, max_size: Optional[str] = None)`

Validates whether the input is a file that is of a certain size or not.

```python
v.size('1KB').validate(filename)  # Must have at least 1KB size
v.size('1MB', '2MB').validate(filename)  # Must have the size between 1MB and 2MB
v.size(None, '1GB').validate(filename)  # Must not be greater than 1GB
v.size(max_size='1GB').validate(filename)  # Must not be greater than 1GB
```

Sizes are not case-sensitive and the accepted values are:

- B
- KB
- MB
- GB
- TB
- PB
- EB
- ZB
- YB

Message template for this validator includes `{min_size}` and `{max_size}`.

## Categorization

- File system

## Changelog

Version | Description
--------|-------------
  1.0.0 | Created

***
See also:

- [Directory](Directory.md)
- [Executable](Executable.md)
- [Exists](Exists.md)
- [Extension](Extension.md)
- [File](File.md)
- [Image](Image.md)
- [Mimetype](Mimetype.md)
- [Readable](Readable.md)
- [SymbolicLink](SymbolicLink.md)
- [Writable](Writable.md)