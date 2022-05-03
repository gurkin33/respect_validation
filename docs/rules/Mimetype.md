# Mimetype

- `Mimetype(mimetype: str)`

Validates if the input is a file and if its MIME type matches the expected one.

```python
v.mimetype('image/png').validate('image.png')  # true
v.mimetype('image/jpeg').validate('image.jpg')  # true
```

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
- [Readable](Readable.md)
- [Size](Size.md)
- [SymbolicLink](SymbolicLink.md)
- [Writable](Writable.md)